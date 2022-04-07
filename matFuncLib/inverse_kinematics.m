function [wl, wr] = inverse_kinematics(u, q)
% Compute the left and right wheel velocities (wl, wr) required for the robot
% to achieve a forward speed u and angular speed q.

% The scale parameter and wheel base required to solve this are provided here.
% You can find these values in the robot simulator as well.
% In real-life, you would have to measure or calibrate them!
scale_parameter = 5.33e-3;
% scale_parameter = 0.0045;
wheel_base = 0.156;
% wheel_base = 0.116;
M = [1, -wheel_base/2; 1, wheel_base/2];
w = M*[u;q]/scale_parameter;
wl = round(w(1));
wr = round(w(2));
if (abs(wl)>100)||(abs(wr)>100)
    error("output exceed threshold");
end

end