[B, A] = butter(20, 0.3, 'low');
%apply Butter filter
filtered = filter(B,A,data);