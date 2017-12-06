function filtersound(file)

Fs = 44100;
load(file) %remove this line when copying the entire script to test for sound
%%data = trim_cardboard_vol15;% the data name

[B, A] = butter(20, 0.3, 'low');
%apply Butter filter
filtered = filter(B,A,data);
sound(filtered,Fs);