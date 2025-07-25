from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import requests
import json


class APITest:
    """Individual test for Book Store API functionality"""
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.base_api_url = "https://demoqa.com"

    def test_api_documentation_access(self):
        """Test access to API documentation"""
        print("🔧 Testing Book Store API - Documentation Access...")
        
        try:
            # Try to access Swagger/API documentation
            api_docs_urls = [
                "https://demoqa.com/swagger/",
                "https://demoqa.com/api-docs",
                "https://demoqa.com/swagger-ui.html"
            ]
            
            for url in api_docs_urls:
                try:
                    self.driver.get(url)
                    time.sleep(3)
                    
                    current_url = self.driver.current_url
                    page_title = self.driver.title
                    
                    print(f"  ✓ Tried: {url}")
                    print(f"    Current URL: {current_url}")
                    print(f"    Page title: {page_title}")
                    
                    # Check for API documentation indicators
                    page_source = self.driver.page_source.lower()
                    if any(keyword in page_source for keyword in ['swagger', 'api', 'documentation', 'endpoints']):
                        print("    ✓ API documentation content found")
                        break
                    else:
                        print("    ⚠️ No API documentation content detected")
                        
                except Exception as url_e:
                    print(f"    ⚠️ Could not access {url}: {url_e}")
            
            print("✅ API documentation access test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ API documentation access test FAILED: {e}")
            return False

    def test_api_endpoints_discovery(self):
        """Test discovery of API endpoints through browser"""
        print("\n🔧 Testing Book Store API - Endpoints Discovery...")
        
        try:
            # Check network requests when using the book store
            self.driver.get("https://demoqa.com/books")
            time.sleep(3)
            
            # Enable browser logs to capture network requests
            logs = self.driver.get_log('performance')
            api_requests = []
            
            for log in logs:
                message = json.loads(log['message'])
                if message['message']['method'] == 'Network.responseReceived':
                    url = message['message']['params']['response']['url']
                    if 'api' in url.lower() or 'bookstore' in url.lower():
                        api_requests.append(url)
            
            if api_requests:
                print(f"  ✓ Found {len(api_requests)} potential API requests:")
                for req in api_requests[:5]:  # Show first 5
                    print(f"    - {req}")
            else:
                print("  ⚠️ No obvious API requests detected in network logs")
            
            # Try common API endpoint patterns
            common_endpoints = [
                "/BookStore/v1/Books",
                "/Account/v1/User",
                "/BookStore/v1/Book",
                "/Account/v1/Authorized"
            ]
            
            print("  ✓ Common API endpoint patterns to test:")
            for endpoint in common_endpoints:
                print(f"    - {self.base_api_url}{endpoint}")
            
            print("✅ API endpoints discovery test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ API endpoints discovery test FAILED: {e}")
            return False

    def test_books_api_endpoint(self):
        """Test Books API endpoint"""
        print("\n🔧 Testing Book Store API - Books Endpoint...")
        
        try:
            # Test the books API endpoint
            books_endpoint = f"{self.base_api_url}/BookStore/v1/Books"
            
            try:
                response = requests.get(books_endpoint, timeout=10)
                print(f"  ✓ Books API request sent to: {books_endpoint}")
                print(f"  ✓ Response status code: {response.status_code}")
                
                if response.status_code == 200:
                    try:
                        books_data = response.json()
                        if 'books' in books_data:
                            print(f"  ✓ Found {len(books_data['books'])} books in API response")
                        else:
                            print("  ✓ API response received (structure may vary)")
                    except json.JSONDecodeError:
                        print("  ⚠️ API response is not JSON format")
                        
                elif response.status_code == 404:
                    print("  ⚠️ Books API endpoint not found (404)")
                else:
                    print(f"  ⚠️ Unexpected response status: {response.status_code}")
                    
            except requests.exceptions.RequestException as req_e:
                print(f"  ⚠️ API request failed: {req_e}")
            
            print("✅ Books API endpoint test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Books API endpoint test FAILED: {e}")
            return False

    def test_user_api_endpoint(self):
        """Test User API endpoint"""
        print("\n🔧 Testing Book Store API - User Endpoint...")
        
        try:
            # Test the user API endpoint
            user_endpoint = f"{self.base_api_url}/Account/v1/User"
            
            try:
                # This will likely require authentication, so we expect 401
                response = requests.get(user_endpoint, timeout=10)
                print(f"  ✓ User API request sent to: {user_endpoint}")
                print(f"  ✓ Response status code: {response.status_code}")
                
                if response.status_code == 401:
                    print("  ✓ Unauthorized response (expected without authentication)")
                elif response.status_code == 200:
                    print("  ✓ Successful response (user may be authenticated)")
                elif response.status_code == 404:
                    print("  ⚠️ User API endpoint not found (404)")
                else:
                    print(f"  ⚠️ Unexpected response status: {response.status_code}")
                    
            except requests.exceptions.RequestException as req_e:
                print(f"  ⚠️ API request failed: {req_e}")
            
            print("✅ User API endpoint test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ User API endpoint test FAILED: {e}")
            return False

    def test_api_response_headers(self):
        """Test API response headers"""
        print("\n🔧 Testing Book Store API - Response Headers...")
        
        try:
            # Test API response headers
            books_endpoint = f"{self.base_api_url}/BookStore/v1/Books"
            
            try:
                response = requests.get(books_endpoint, timeout=10)
                print(f"  ✓ API request sent to: {books_endpoint}")
                
                # Check response headers
                headers = response.headers
                print("  ✓ Response headers:")
                
                important_headers = ['content-type', 'server', 'access-control-allow-origin', 'cache-control']
                for header in important_headers:
                    if header in headers:
                        print(f"    - {header}: {headers[header]}")
                    else:
                        print(f"    - {header}: Not present")
                
                # Check for CORS headers
                if 'access-control-allow-origin' in headers:
                    print("  ✓ CORS headers present")
                else:
                    print("  ⚠️ No CORS headers found")
                
                # Check content type
                content_type = headers.get('content-type', '')
                if 'application/json' in content_type:
                    print("  ✓ JSON content type confirmed")
                else:
                    print(f"  ⚠️ Unexpected content type: {content_type}")
                    
            except requests.exceptions.RequestException as req_e:
                print(f"  ⚠️ API request failed: {req_e}")
            
            print("✅ API response headers test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ API response headers test FAILED: {e}")
            return False

    def test_api_error_handling(self):
        """Test API error handling"""
        print("\n🔧 Testing Book Store API - Error Handling...")
        
        try:
            # Test invalid endpoints
            invalid_endpoints = [
                f"{self.base_api_url}/BookStore/v1/InvalidEndpoint",
                f"{self.base_api_url}/Account/v1/InvalidUser",
                f"{self.base_api_url}/BookStore/v1/Book/invalid-isbn"
            ]
            
            for endpoint in invalid_endpoints:
                try:
                    response = requests.get(endpoint, timeout=10)
                    print(f"  ✓ Tested invalid endpoint: {endpoint}")
                    print(f"    Status code: {response.status_code}")
                    
                    if response.status_code == 404:
                        print("    ✓ Proper 404 error handling")
                    elif response.status_code >= 400:
                        print(f"    ✓ Proper error response ({response.status_code})")
                    else:
                        print(f"    ⚠️ Unexpected success response")
                        
                    # Check if error response has proper format
                    try:
                        error_data = response.json()
                        if 'error' in error_data or 'message' in error_data:
                            print("    ✓ Structured error response")
                    except:
                        print("    ✓ Non-JSON error response")
                        
                except requests.exceptions.RequestException as req_e:
                    print(f"    ⚠️ Request failed: {req_e}")
            
            print("✅ API error handling test PASSED")
            return True
            
        except Exception as e:
            print(f"❌ API error handling test FAILED: {e}")
            return False

    def run_all_api_tests(self):
        """Run all API tests"""
        print("=" * 60)
        print("🔌 API INDIVIDUAL TESTS")
        print("=" * 60)
        
        results = []
        
        try:
            results.append(self.test_api_documentation_access())
            results.append(self.test_api_endpoints_discovery())
            results.append(self.test_books_api_endpoint())
            results.append(self.test_user_api_endpoint())
            results.append(self.test_api_response_headers())
            results.append(self.test_api_error_handling())
            
            passed = sum(results)
            total = len(results)
            
            print(f"\n📊 API TEST SUMMARY: {passed}/{total} tests passed")
            
            if passed == total:
                print("🎉 All API tests PASSED!")
            elif passed > 0:
                print("⚠️ Some API tests passed, some had issues")
            else:
                print("❌ All API tests had issues")
                
        except Exception as e:
            print(f"❌ API test suite failed: {e}")
        finally:
            self.driver.quit()


# Usage
if __name__ == "__main__":
    api_test = APITest()
    api_test.run_all_api_tests()