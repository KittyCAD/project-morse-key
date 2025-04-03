#ifndef MORSE_TRANSLATOR_H
#define MORSE_TRANSLATOR_H

#include "LedManager.h"
#include <Arduino.h>

struct MorseTableEntry {
    const char* code;
    char character;
};

class MorseTranslator {
  private:
    // Button control.
    bool buttonPressed;
    int lastButtonState;
    unsigned long lastDebounceTime;
    unsigned long pressStartTime;
    unsigned long pressEndTime;
    unsigned long lastReleaseTime;

    // Pin assignments.
    int idPinRead;
    int idPinLed;
    int idPinBuzzer;

    // Timing parameters.
    int frequencyBuzzer;
    unsigned long durationDash;
    unsigned long gapInterLetter;
    unsigned long gapInterWord;
    unsigned long delayDebounce;

    // LED flasher.
    LedManager ledManager;

    // Morse buffer and table reference.
    String morseBuffer;
    const MorseTableEntry* morseTable;
    int morseEntries;

  public:
    MorseTranslator (const MorseTableEntry* morse_table, int morse_entries);

    void initialize ();
    void processMorse ();
    void translateMorse (const String& morse);
    void handleButtonPress (bool isPressed, unsigned long currentTime);
    void checkForLetterOrWord (unsigned long currentTime);
    void soundBuzzer (bool on);
};

#endif