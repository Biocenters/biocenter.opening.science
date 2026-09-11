"""The external service must only be reachable after the local notice."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
TARGET = 'https://opendrop.151-115-76-163.sslip.io/'

class Page(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.tags = []
        self.feed((ROOT / filename).read_text())
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

class ExitNoticeTests(unittest.TestCase):
    def test_both_entries_go_to_notice(self):
        links = [a for t, a in Page('index.html').tags if t == 'a']
        self.assertEqual(sum(a.get('href') == '/external-control.html' for a in links), 2)
        self.assertFalse(any('sslip.io' in a.get('href', '') for a in links))

    def test_no_automatic_external_connection_or_redirect(self):
        page = Page('external-control.html')
        self.assertFalse(any(t in ('script', 'iframe', 'form', 'object', 'embed') for t, _ in page.tags))
        for tag, attrs in page.tags:
            self.assertNotIn(attrs.get('rel'), ('preconnect', 'prefetch', 'dns-prefetch', 'prerender'))
            self.assertNotEqual(attrs.get('http-equiv', '').lower(), 'refresh')
            if tag != 'a':
                self.assertFalse(any(v and v.startswith(('http:', 'https:', '//')) for k,v in attrs.items() if k in ('src','href','data')))
        links = [a for t,a in page.tags if t == 'a']
        outbound = [a for a in links if a.get('href','').startswith('https:')]
        self.assertEqual(len(outbound), 1)
        self.assertEqual(outbound[0]['href'], TARGET)
        self.assertEqual(outbound[0]['referrerpolicy'], 'no-referrer')
        self.assertNotIn('target', outbound[0])
        self.assertTrue(any(a.get('href') == '/#prototype' for a in links))
        self.assertEqual(sum(t == 'main' for t,_ in page.tags), 1)
        self.assertEqual(sum(t == 'h1' for t,_ in page.tags), 1)
        self.assertIn(TARGET + '</span>', (ROOT / 'external-control.html').read_text())

    def test_copied_base_stays_in_sync(self):
        index = (ROOT / 'index.html').read_text()
        base = index.split('<style>', 1)[1].split('/* --- Skip link', 1)[0].strip()
        self.assertIn(base, (ROOT / 'external-control.html').read_text())

if __name__ == '__main__':
    unittest.main()
