'''
Changes i made
1. Created two test functions google_translator() and detect() with print statements
    to make sure they are properly called within the api function.
2. Removed the if statement checking the length of 'word', it works similar to 
    the 'not word' if statement, so no need for repeated logic.
3. Imported re
'''
import re
def google_translator():
    print('Google_translate called.')
def detect():
    print('Language detected')

def api(word):
    try:
        if not word:
            return {
                "message": "String is empty or invalid",
                "success": False,
                "input_string": word
            }
        if not re.search('[a-zA-Z]', word):
            return {
                "message": "String invalid characters",
                "success": False,
                "input_string": word
            }
        detector = google_translator()
        return_data = list()
        language_list = []
        for item in word.split(' '):
            detect_result = detector.detect(item)
            print(detect_result)
            return_data.append(
                {
                    "input_string": item,
                    "short_form": detect_result[0],
                    "long_form": detect_result[1]
                }
            )
            language_list.append(detect_result[0])

        return {
            "data": return_data,
            "success": True,
            "input_string": word,
            "same_language": len(set(language_list)) == 1
        }
    except Exception as e:
        print(e)
        return {
            "message": "String is empty or invalid",
            "success": False
        }