import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from oscillator import make_time_array, sine_oscillator

SAMPLE_RATE = 44100


def additive_synth(
    fundamental: float,
    num_partials: int,
    duration: float,
    amplitudes: list = None,  # if None, use 1/n falloff
    sample_rate: int = SAMPLE_RATE,
) -> np.ndarray:

    if amplitudes is None:
        amplitudes = [1.0 / n for n in range(1, num_partials + 1)]

    assert len(amplitudes) == num_partials, "Need one amplitude per partial"

    output = np.zeros(int(sample_rate * duration))

    for n in range(1, num_partials + 1):
        freq = fundamental * n
        amp = amplitudes[n - 1]

        # Stop if partial exceeds Nyquist - beyond this is aliasing
        if freq >= sample_rate / 2:
            print(f"Partial {n} at {freq}Hz exceeds Nyquist - Skipping")
            break

        output += sine_oscillator(freq, amp, duration, sample_rate=sample_rate)

    # Normalize to [-1, 1]
    peak = np.max(np.abs(output))
    if peak > 0:
        output /= peak

    return output


if __name__ == "__main__":
    duration = 2.0
    fundamental = 440.0
    num_partials = 10

    wave = additive_synth(fundamental, num_partials, duration)
    sf.write("additive_440.wav", wave.astype(np.float32), SAMPLE_RATE, subtype="FLOAT")
    print("Written: additive_440.wav")

    # Plot first 5ms
    samples_5ms = int(SAMPLE_RATE * 0.005)
    t = make_time_array(duration)
    plt.plot(t[:samples_5ms], wave[:samples_5ms])
    plt.title(f"Additive — {num_partials} partials, fundamental {fundamental}Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.savefig("additive_440.png")
    print("Plot saved: additive_440.png")
