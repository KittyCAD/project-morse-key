#include "MorseTranslator.h"
#include "morse_table.h"
#include <Arduino.h>

MorseTranslator translator (MORSE_TABLE, MORSE_ENTRIES);

void setup () {
    translator.initialize ();
}

void loop () {
    translator.processMorse ();
}