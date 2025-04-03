#include "MorseTranslator.h"
#include "Keyboard.h"
#include "constants.h"

MorseTranslator::MorseTranslator (const MorseTableEntry* morseTable, int morseEntries)
    : buttonPressed (false)
    , lastButtonState (HIGH)
    , lastDebounceTime (0)
    , pressStartTime (0)
    , pressEndTime (0)
    , lastReleaseTime (0)

    , idPinRead (Constants::ID_PIN_READ)
    , idPinLed (Constants::ID_PIN_LED)
    , idPinBuzzer (Constants::ID_PIN_BUZZER)

    , frequencyBuzzer (Constants::BUZZER_FREQ)
    , durationDash (Constants::DURATION_DASH)
    , gapInterLetter (Constants::GAP_INTER_LETTER)
    , gapInterWord (Constants::GAP_INTER_WORD)
    , delayDebounce (Constants::DEBOUNCE_DELAY)

    , ledManager (Constants::ID_PIN_LED)

    , morseBuffer ("")
    , morseTable (morseTable)
    , morseEntries (morseEntries) {
}

void MorseTranslator::initialize () {
    Serial.begin (Constants::SERIAL_BAUD);

    Keyboard.begin ();
    Serial.println ("Keyboard support enabled...");

    pinMode (idPinRead, INPUT_PULLUP);
    ledManager.initialize ();
    ledManager.setState (LED_BLINKING);

    Serial.println ("Ready...");
}

void MorseTranslator::processMorse () {
    unsigned long currentTime = millis ();

    // Update LED state.
    ledManager.update ();


    int currentButtonState = digitalRead (idPinRead);

    if (currentButtonState != lastButtonState) {
        lastDebounceTime = currentTime;
    }

    if ((currentTime - lastDebounceTime) > delayDebounce) {
        int debouncedButtonState = currentButtonState;
        handleButtonPress (debouncedButtonState == LOW, currentTime);
    }

    lastButtonState = currentButtonState;
    checkForLetterOrWord (currentTime);
}

void MorseTranslator::handleButtonPress (bool isPressed, unsigned long currentTime) {
    if (isPressed) {
        ledManager.setState (LED_ON);
        soundBuzzer (true);

        // If this is a new button press.
        if (!buttonPressed) {
            buttonPressed  = true;
            pressStartTime = currentTime;
        }
    }

    else {
        // Turn off the LED and reset to the default blink state.
        if (ledManager.getState () != LED_BLINKING) {
            ledManager.setState (LED_BLINKING);
        }
        soundBuzzer (false);

        // If button was just released...
        if (buttonPressed) {
            buttonPressed               = false;
            pressEndTime                = currentTime;
            unsigned long pressDuration = pressEndTime - pressStartTime;

            // Check dot vs. dash.
            if (pressDuration < durationDash) {
                morseBuffer += ".";
                Serial.print (".");
            } else {
                morseBuffer += "-";
                Serial.print ("-");
            }

            lastReleaseTime = pressEndTime;
        }
    }
}

void MorseTranslator::checkForLetterOrWord (unsigned long currentTime) {
    unsigned long timeSinceRelease = currentTime - lastReleaseTime;

    if (lastReleaseTime > 0 && !buttonPressed) {
        if (timeSinceRelease > gapInterWord) {
            // Translate and reset buffer.
            translateMorse (morseBuffer);
            morseBuffer = "";
            Serial.print (" "); // Word space.
            Keyboard.write (' ');
            lastReleaseTime = 0;
        } else if (timeSinceRelease > gapInterLetter && morseBuffer.length () > 0) {
            // Translate and reset buffer.
            translateMorse (morseBuffer);
            morseBuffer     = "";
            lastReleaseTime = 0;
        }
    }
}

void MorseTranslator::translateMorse (const String& morse) {
    bool found = false;

    for (int i = 0; i < morseEntries; i++) {
        if (morse.equals (morseTable[i].code)) {
            Serial.print (morseTable[i].character);
            Keyboard.write (morseTable[i].character);
            found = true;
            break;
        }
    }

    if (!found) {
        Serial.print ("?");
    }
}

void MorseTranslator::soundBuzzer (bool on) {
    if (on) {
        tone (idPinBuzzer, frequencyBuzzer);
    } else {
        noTone (idPinBuzzer);
    }
}