function plot_original(file)
load(file)
Fs = 44100
a = abs(fft(data));
figure(1)
num_bins = length(a);
plot([0:1/(num_bins/2 -1):1], a(1:num_bins/2))
%plot(a(1:1000))
title('FFT of Original Data')
xlabel('Normalised frequency')
ylabel('Magnitude')
figure(2)
plot(data)
xlabel('Time')
ylabel('Amplitude')
title('Original data')
sound(data, Fs)