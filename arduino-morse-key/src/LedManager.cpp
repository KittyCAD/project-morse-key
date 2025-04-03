#include "LedManager.h"

LedManager::LedManager (uint8_t ledPin, unsigned long blinkIntervalMs, unsigned long onDurationMs)
    : pin (ledPin)
    , currentState (LED_OFF)
    , blinkInterval (blinkIntervalMs)
    , onDuration (onDurationMs)
    , lastBlinkTime (0)
    , blinkState (false) {
}

void LedManager::initialize () {
    pinMode (pin, OUTPUT);
    digitalWrite (pin, LOW);
}

void LedManager::update () {
    unsigned long currentTime = millis ();

    // Update LED based on current state.
    switch (currentState) {
    case LED_OFF: digitalWrite (pin, LOW); break;

    case LED_ON: digitalWrite (pin, HIGH); break;

    case LED_BLINKING:
        if (blinkState) {
            // LED is currently on, check if it's time to turn it off.
            if (currentTime - lastBlinkTime >= onDuration) {
                blinkState = false;
                digitalWrite (pin, LOW);
            }
        } else {
            // LED is currently off, check if it's time for next blink.
            if (currentTime - lastBlinkTime >= blinkInterval) {
                blinkState = true;
                digitalWrite (pin, HIGH);
                lastBlinkTime = currentTime;
            }
        }
        break;
    }
}

void LedManager::setState (LedState newState) {
    if (currentState != newState) {
        currentState = newState;

        if (newState == LED_BLINKING) {
            lastBlinkTime = millis ();
            blinkState    = true;
            digitalWrite (pin, HIGH);
        } else if (newState == LED_ON) {
            digitalWrite (pin, HIGH);
        } else if (newState == LED_OFF) {
            digitalWrite (pin, LOW);
        }
    }
}

LedState LedManager::getState () {
    return currentState;
}

void LedManager::setBlinkInterval (unsigned long intervalMs) {
    blinkInterval = intervalMs;
}

void LedManager::setOnDuration (unsigned long durationMs) {
    onDuration = durationMs;
}