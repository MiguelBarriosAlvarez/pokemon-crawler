import requests
import responses
import unittest

# Create your tests here.
class Test_Request(unittest.TestCase):

    @responses.activate
    def testExample(self):
        responses.add(**{
            'method': responses.GET,
            'url': 'https://pokeapi.co/api/v2/pokemon/',
            'body': '{"error": "reason"}',
            'status': 404,
            'content_type': 'application/json',
            'adding_headers': {'X-Foo': 'Bar'}
        })
        response = requests.get('https://www.bing.com/images/search?q="mercedes"&FORM=HDRSC2')
        self.assertEqual({'error': 'reason'}, response.json())
        self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
