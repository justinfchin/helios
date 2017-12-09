function mat_wav(file)

Fs = 44100;
load(file)

%Butter filter
%[B, A] = butter(20, 0.4, 'low');
%apply Butter filter
%filtered = filter(B,A,data);
%filename = 'filtered_male5cb.wav';
%audiowrite(filename,filtered*50,Fs)

%raw data from ldv
%filename = 'male5cb_LDVraw.wav';
%audiowrite(filename,data*50,Fs);

for n = 1:441000
    if (abs(data(n))< .003)
        data(n) = data(n)/2;
    end
end

%%%%
%create Butter filter co
[B, A] = butter(20, 0.4, 'low');
%apply Butter filter
filtered = filter(B,A,data);

filename = 'our_male5cb.wav';
audiowrite(filename,filtered*100,Fs);
