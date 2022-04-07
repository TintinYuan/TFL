function [a, b, sigma]=linear_regression(x,y,x_label,y_label)
    % calaulate the mean of the data
    xMean = mean(x);
    yMean = mean(y);
    
    % covarince of the variables
    Sxy = sum((x-xMean).*(y-yMean));
    Sxx = sum((x-xMean).^2);
    
    % solve for parameters
    a = Sxy/Sxx;
    b = yMean - a*xMean;
    sigma = mean((y-a*x-b).^2);
    
    % visualise the result
    figure;
    f = @(z)a*z+b;
    plot(x, y, 'b.');
    hold on
    % adjust the axis
    if min(x) < 0
        fplot(f,[min(x), max(x)]);
    else
        fplot(f,[0, max(x)]);
    end
    % display the label
    xlabel(x_label,'Interpreter', 'latex');
    ylabel(y_label,'Interpreter', 'latex');
    grid on
    
end