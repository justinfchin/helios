function ourfilter(file)
close all
clear sound
Fs = 44100;
load(file)
data1 = data;
data2 = data;
for n = 1:440999
    if (abs(data(n))< .003)
        data(n) = data(n)/2;
    end
end

%%%%
%create Butter filter co
[B, A] = butter(20, 0.4, 'low');
%apply Butter filter
filtered = filter(B,A,data);

%for n = 1:441000
%    if (abs(filtered(n))< .005)
%        filtered(n) = filtered(n)/6;
%    end
%end

%Regular butter
[B, A] = butter(20, 0.4, 'low');
%apply Butter filter
data2 = filter(B,A,data2);

%lets see how this compares with the fft of input
b = abs(fft(filtered));
figure(2)
num_bins = length(b);
plot([0:1/(num_bins/2 -1):1], b(1:num_bins/2))
title('FFT of Butter filtered data')
xlabel('Normalised frequency')
ylabel('Magnitude')
%testing the sound difference
%1st sound is original
%2nd sound is filtered
%sound(data,Fs);
%sound(filtered,Fs);
figure(3)
plot(data1)
xlabel('Time')
ylabel('Amplitude')
title('Raw data from LDV')
figure(4)
plot(filtered)
xlabel('Time')
ylabel('Amplitude')
title('Filtered Data with Our+Butter')

figure(5)
plot(data2)
xlabel('Time')
ylabel('Amplitude')
title('Filtered Data with Butter')


%testing the sound difference
%1st sound is original
%2nd sound is filtered
%sound(data,Fs);
sound(filtered*50,Fs);
