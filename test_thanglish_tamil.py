import pytest
from playwright.sync_api import Page, expect
import time 

test_cases = [
    {
        "id": "Pos_Fun_0001",
        "name": "Convert a short daily greeting",
        "input": "vanakkam!",
        "expected": "வணக்கம்!",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0002",
        "name": "Convert a simple daily statement",
        "input": "naan veetukku pogiren.",
        "expected": "நான் வீட்டுக்கு போகிறேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0003",
        "name": "Convert a short interrogative question",
        "input": "neenga eppadi irukeenga?",
        "expected": "நீங்க எப்படி இருக்கீங்க?",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0004",
        "name": "Convert a simple imperative command",
        "input": "inge vaanga.",
        "expected": "இங்கே வாங்க.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0005",
        "name": "Convert a short request phrase",
        "input": "enakku udhavi pannunga.",
        "expected": "எனக்கு உதவி பண்ணுங்க.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0006",
        "name": "Convert a future tense sentence",
        "input": "naan varuven.",
        "expected": "நான் வருவேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0007",
        "name": "Convert a negative form sentence",
        "input": "naan vara maatten.",
        "expected": "நான் வர மாட்டேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0008",
        "name": "Convert a past tense sentence",
        "input": "naan netruponen.",
        "expected": "நான் நேற்று போனேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0009",
        "name": "Convert a present tense sentence",
        "input": "naan ippo velai seigiren.",
        "expected": "நான் இப்போ வேலை செய்கிறேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0010",
        "name": "Convert a compound sentence",
        "input": "naan saapiduven, appuram padam paapen.",
        "expected": "நான் சாப்பிடுவேன், அப்புறம் படம் பாப்பேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0011",
        "name": "Convert a complex sentence",
        "input": "mazhai peythaal naan veliye poga maatten.",
        "expected": "மழை பெய்தால் நான் வெளியே போக மாட்டேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0012",
        "name": "Convert a polite request",
        "input": "thayavu seidhu enakku udhavi pannunga.",
        "expected": "தயவு செய்து எனக்கு உதவி பண்ணுங்க.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0013",
        "name": "Convert informal phrasing",
        "input": "seri daa, varen.",
        "expected": "சரி டா, வரேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0014",
        "name": "Multi-word expression",
        "input": "romba nandri.",
        "expected": "ரொம்ப நன்றி.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0015",
        "name": "Repeated words for emphasis",
        "input": "seekiram seekiram vaa.",
        "expected": "சீக்கிரம் சீக்கிரம் வா.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0016",
        "name": "Pronoun variation (Plural)",
        "input": "naanga nalaiku varom.",
        "expected": "நாங்கள் நாளைக்கு வரோம்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0017",
        "name": "Proper word spacing",
        "input": "naan ungalai paarkiren.",
        "expected": "நான் உங்களை பார்க்கிறேன்",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0018",
        "name": "Convert a simple question about health",
        "input": "ungalukku udambu eppadi irukku?",
        "expected": "உங்களுக்கு உடம்பு எப்படி இருக்கு?",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0019",
        "name": "Convert a statement about time/arrival",
        "input": "naan ippo thaan vandhen.",
        "expected": "நான் இப்போ தான் வந்தேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0020",
        "name": "Convert a request for food",
        "input": "enakku saapaadu konjam kudu.",
        "expected": "எனக்கு சாப்பாடு கொஞ்சம் குடு.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0021",
        "name": "Convert a compound sentence about daily routine",
        "input": "naan kulithu vittu, saapida pogiren.",
        "expected": "நான் குளித்து விட்டு, சாப்பிட போகிறேன்",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0022",
        "name": "Convert a complex sentence with a reason",
        "input": "enakku pasikkiradhu adhanaal naan saapiduven.",
        "expected": "எனக்கு பசிக்கிறது அதனால் நான் சாப்பிடுவேன்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0023",
        "name": "Convert a plural statement about friends",
        "input": "en nanbargal ellorum varuvaargal.",
        "expected": "என் நண்பர்கள் எல்லோரும் வருவார்கள்.",
        "type": "positive"
    },
    {
        "id": "Pos_Fun_0024",
        "name": "Convert a polite greeting for a guest",
        "input": "veetukku vaanga, utkaarunga.",
        "expected": "வீட்டுக்கு வாங்க, உட்காருங்க.",
        "type": "positive"
    },
    {
        "id": "Neg_Fun_0001",
        "name": "Common English word should remain unchanged (school)",
        "input": "pasanga school-ku ponaanga.",
        "expected": "பசங்க school-க்கு போனாங்க.",
        "type": "negative"
    },
    {
        "id": "Neg_Fun_0002",
        "name": "Place name should remain in English",
        "input": "naan Chennai la office-ku pogiren.",
        "expected": "நான் Chennai ல office-க்கு போகிறேன்.",
        "type": "negative"
    },
    {
        "id": "Neg_Fun_0003",
        "name": "Brand and technical terms should remain unchanged",
        "input": "WhatsApp la message anuppunga.",
        "expected": "WhatsApp ல message அனுப்புங்க.",
        "type": "negative"
    },
    {
        "id": "Neg_Fun_0004",
        "name": "English abbreviation should remain unchanged",
        "input": "enakku OTP vandhuchu.",
        "expected": "எனக்கு OTP வந்துச்சு",
        "type": "negative"
    },
    {
        "id": "Neg_Fun_0005",
        "name": "Currency format should be preserved",
        "input": "Rs. 1500 kudunga.",
        "expected": "ரூ. 1500 குடுங்க.",
        "type": "negative"
    },
    {
        "id": "Neg_Fun_0006",
        "name": "Date format should be preserved",
        "input": "25/12/2025 leave.",
        "expected": "25/12/2025 leave.",
        "type": "negative"
    },
    {
        "id": "Neg_Fun_0007",
        "name": "Time and unit formats should be preserved",
        "input": "7.30 AM ku vaanga, 2 km nadakkanum.",
        "expected": "7.30 AMக்கு வாங்க, 2 km நடக்கணும்.",
        "type": "negative"
    },
    {
        "id": "Neg_Fun_0008",
        "name": "Very long single word (No breaks)",
        "input": "ungalukkuthaanidhaichollavandhen",
        "expected": "உங்களுக்குத் தான் இதைச் சொல்ல வந்தேன்",
        "type": "negative"
    },
    {
        "id": "Neg_Fun_0009",
        "name": "English technical abbreviations should remain unchanged",
        "input": "enoda PC la RAM kammi.",
        "expected": "என்னோட PC ல RAM கம்மி.",
        "type": "negative"
    },
    {
        "id": "Neg_Fun_0010",
        "name": "Numbers and measurement units should be preserved",
        "input": "5 kg sakkarai venum.",
        "expected": "5 kg சர்க்கரை வேண்டும்.",
        "type": "negative"
    },
    {
        "id": "Pos_UI_0001",
        "name": "Real-time output update",
        "input": "naan varuven",
        "expected": "நான் வருவேன்",
        "type": "ui"
    }
]

class TestThanglishToTamil:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Navigate to the website before each test"""
        page.goto("https://tamil.changathi.com/")
        time.sleep(2)

    @pytest.mark.parametrize("test_data", test_cases)
    def test_transliteration(self, page: Page, test_data):
        """Test each transliteration case"""

        textarea = page.locator("#transliterateTextarea")

        textarea.fill("")
        time.sleep(0.5)

        textarea.type(test_data["input"], delay=50)
        time.sleep(1)

        actual_output = textarea.input_value()

        print(f"\n{'='*80}")
        print(f"Test ID: {test_data['id']}")
        print(f"Test Name: {test_data['name']}")
        print(f"Input: {test_data['input']}")
        print(f"Expected: {test_data['expected']}")
        print(f"Actual: {actual_output}")
        print(f"Type: {test_data['type']}")
        print(f"{'='*80}")
        
        if test_data["type"] == "positive":
            assert actual_output == test_data["expected"], \
            f"FAIL: Expected '{test_data['expected']}' but got '{actual_output}'"
        else:
            assert actual_output != test_data["expected"], \
           f"FAIL: Negative test passed unexpectedly. Output: '{actual_output}'"
    
    def test_ui_realtime_update(self, page: Page):
        """Test UI real-time update behavior (Pos_UI_0001)"""

        textarea = page.locator("#transliterateTextarea")

        textarea.fill("")
        time.sleep(0.5)

        textarea.type("naan varuven", delay=100)

        time.sleep(1)
        actual_output = textarea.input_value()

        print(f"\n{'='*80}")
        print(f"Test ID: Pos_UI_0001")
        print(f"Test Name: Real-time output update")
        print(f"Output after typing: {actual_output}")
        print(f"{'='*80}")

        assert len(actual_output) > 0, "Output field did not update in real-time"
        assert actual_output != "naan varuven", "Output should be converted to Tamil"
