function specialfilter(file)

Fs = 44100;
load(file) %remove this line when copying the entire script to test for sound
%%data = trim_cardboard_vol15;% the data name

[B, A] = butter(20, 0.11, 'low');
%apply Butter filter
filtered = filter(B,A,data);

b = abs(fft(filtered));
figure(1)
num_bins = length(b);
plot([0:1/(num_bins/2 -1):1], b(1:num_bins/2))
title('FFT of Butter filtered data')
xlabel('Normalised frequency')
ylabel('Magnitude')
filtered = filtered*50;

figure(2)
plot(filtered)
sound(filtered,Fs)