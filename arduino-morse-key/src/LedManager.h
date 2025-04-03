#ifndef LED_MANAGER_H
#define LED_MANAGER_H

#include <Arduino.h>

enum LedState { LED_OFF, LED_ON, LED_BLINKING };

class LedManager {
  private:
    uint8_t pin;
    LedState currentState;
    unsigned long blinkInterval; // Total time between blink starts (milliseconds).
    unsigned long onDuration; // Duration LED stays on during blink (milliseconds).
    unsigned long lastBlinkTime; // Last time the LED state was toggled.
    bool blinkState;             // Current state within blink cycle.

  public:
    LedManager (uint8_t ledPin, unsigned long blinkIntervalMs = 1000, unsigned long onDurationMs = 200);
    void initialize ();
    void update ();
    void setState (LedState newState);
    LedState getState ();
    void setBlinkInterval (unsigned long intervalMs);
    void setOnDuration (unsigned long durationMs);
};

#endif // LED_MANAGER_H