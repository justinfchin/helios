function ProcessWaves(file)
Fs = 44100;
load(file) %remove this line when copying the entire script to test for sound
data = trim_cardboard_vol15;% the data name

a = abs(fft(data));
figure(1)
num_bins = length(a);
plot([0:1/(num_bins/2 -1):1], a(1:num_bins/2))
%plot(a(1:1000))
xlabel('Normalised frequency (\pi rads/sample)')
ylabel('Magnitude')
%create Butter filter co
[B, A] = butter(2, 0.3, 'low');
%apply Butter filter
filtered = filter(B,A,data);

%lets see how this compares with the fft of input
b = abs(fft(filtered));
figure(2)
num_bins = length(b);
plot([0:1/(num_bins/2 -1):1], b(1:num_bins/2))
xlabel('Normalised frequency (\pi rads/sample)')
ylabel('Magnitude')
%testing the sound difference
%1st sound is original
%2nd sound is filtered
%sound(data,Fs);
%sound(filtered,Fs);





