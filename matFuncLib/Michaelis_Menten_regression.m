function [a, b, sigma]=Michaelis_Menten_regression(x,y,x_label,y_label)
    % calaulate the mean of the data
    x_rec = 1./x;
    y_rec = 1./y;
    xMean = mean(x_rec);
    yMean = mean(y_rec);
    
    % covarince of the variables
    Sxy = sum((x_rec-xMean).*(y_rec-yMean));
    Sxx = sum((x_rec-xMean).^2);
    
    % solve for parameters
    a = Sxy/Sxx;
    b = yMean - a*xMean;
    sigma = mean((y_rec-a*x-b).^2);
    
    b = 1/b;
    a = a*b;
    
    % visualise the result
    figure;
    f = @(z)b*z/(z+a);
    plot(x, y,'b.','MarkerSize',16)
    axis([(min(x)-10) (max(x)+10) (min(y)-0.1*mean(y)) (max(y)+0.1*mean(y))])
    hold on
    % adjust the axis
    fplot(f,[(min(x)-0.2*(max(x)-min(x))), max(x)+ 0.2*(max(x)-min(x))]);
    % display the label
    xlabel(x_label);
    ylabel(y_label);
    grid on
    
end