function ProcessWaves(file)

load(file)
a = abs(fft(data));
a = a(1:floor(length(a)/2)); %Split data in half since waves are mirrored
%plot(a)
figure
plot(a(1:1000)) %1 to 1000 herzs interval
