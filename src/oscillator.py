import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100


def make_time_array(duration: float, sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    """
    Returns an array of time values from 0 to duration (seconds).
    """
    return np.linspace(0, duration, int(sample_rate * duration), endpoint=False)


def sine_oscillator(
    freq: float,
    amplitude: float,
    duration: float,
    phase: float = 0.0,
    sample_rate: int = SAMPLE_RATE,
) -> np.ndarray:
    t = make_time_array(duration, sample_rate)
    return amplitude * np.sin(2 * np.pi * freq * t + phase)


if __name__ == "__main__":
    duration = 1.0  # seconds
    freq = 440.0
    amplitude = 0.8

    wave = sine_oscillator(freq, amplitude, duration)

    # Write to WAV
    sf.write("sine_440.wav", wave, SAMPLE_RATE)
    print("Written: sine_440.wav")

    # Plot first 5ms
    sample_5ms = int(SAMPLE_RATE * 0.005)
    t = make_time_array(duration)
    plt.plot(t[:sample_5ms], wave[:sample_5ms])
    plt.title(f"Sine wave — {freq}Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.savefig("sine_440.png")
    print("Plot saved: sine_440.png")
