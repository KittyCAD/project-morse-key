#ifndef CONSTANTS_H
#define CONSTANTS_H

namespace Constants {
// Serial.
constexpr int SERIAL_BAUD = 9600;

// Pin assignments.
// constexpr int ID_PIN_READ   = 22;
constexpr int ID_PIN_READ = 7; // Leonardo.
constexpr int ID_PIN_LED  = LED_BUILTIN;
// constexpr int ID_PIN_BUZZER = 7; // PWM pin.
constexpr int ID_PIN_BUZZER = 3; // PWM pin, Leonardo.

// Buzzer freq.
constexpr int BUZZER_FREQ = 600; // Hz.

// Timing parameters, milliseconds.
constexpr unsigned long DURATION_DOT     = 100;
constexpr unsigned long DURATION_DASH    = DURATION_DOT * 3;
constexpr unsigned long GAP_INTER_LETTER = DURATION_DOT * 3;
constexpr unsigned long GAP_INTER_WORD   = DURATION_DOT * 7;

// Debounce parameters.
constexpr unsigned long DEBOUNCE_DELAY = 20;

// Buffer limits.
constexpr int MAX_BUFFER_SIZE = 20;
} // namespace Constants

#endif