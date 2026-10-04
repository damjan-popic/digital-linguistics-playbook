"""Small regression tests; run with python -m unittest discover -s personal-site."""
import tempfile
import unittest
from pathlib import Path
from build import CONTENT, build, read_page, relative_url, render_markdown, validate

class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.work = tempfile.TemporaryDirectory()
        cls.parent = Path(cls.work.name)
        cls.output = cls.parent / 'damjan'
        (cls.parent / 'playbook-sentinel.txt').write_text('unchanged', encoding='utf-8')
        cls.result = build(cls.output)
    @classmethod
    def tearDownClass(cls):
        cls.work.cleanup()
    def test_all_pages_and_links(self):
        self.assertEqual(self.result[0], len(list(CONTENT.rglob('*.md'))) + 1)
        self.assertEqual(validate(self.output), self.result)
    def test_parent_site_is_untouched(self):
        self.assertEqual((self.parent / 'playbook-sentinel.txt').read_text(), 'unchanged')
    def test_existing_unrelated_directory_is_refused(self):
        with self.assertRaises(ValueError):
            build(self.parent)
        self.assertTrue((self.parent / 'playbook-sentinel.txt').exists())
    def test_source_directory_is_refused(self):
        with self.assertRaises(ValueError):
            build(CONTENT / 'sl')
    def test_relative_links_work_at_any_base_path(self):
        self.assertEqual(relative_url('en/teaching/agrft/', 'sl/poucevanje/agrft/'), '../../../en/teaching/agrft/')
        self.assertEqual(relative_url('assets/style.css', 'sl/'), '../assets/style.css')
        self.assertEqual(relative_url('sl/', ''), 'sl/')
    def test_missing_markdown_link_fails(self):
        page = read_page(CONTENT / 'sl/index.md')
        page['body'] = '[Broken](missing.md)'
        with self.assertRaises(ValueError):
            render_markdown(page, {})
    def test_body_cannot_add_a_second_h1(self):
        page = read_page(CONTENT / 'sl/index.md')
        page['body'] = '# Extra title'
        with self.assertRaises(ValueError):
            render_markdown(page, {})
    def test_duplicate_headings_get_unique_anchors(self):
        page = read_page(CONTENT / 'sl/index.md')
        page['body'] = '## Gradiva\n\nOne\n\n## Gradiva\n\nTwo'
        _, toc = render_markdown(page, {})
        self.assertEqual([x['id'] for x in toc], ['gradiva', 'gradiva-2'])

if __name__ == '__main__':
    unittest.main()
