

n=40000;%要读入的行数
 
fid=fopen('d2d_sinr_random.txt'); 
for i=1:n
    d2d_sinr_random_2(i)=str2double(fgets(fid));
end 
fclose(fid);



fid=fopen('d2d_rate_random.txt'); 
for i=1:n
    d2d_rate_random_2(i)=str2double(fgets(fid));
end 
fclose(fid);

fid=fopen('d2d_sinr_rl.txt'); 
for i=1:n
    d2d_sinr_rl(i)=str2double(fgets(fid));
end 
fclose(fid);
figure(1);
h1=cdfplot(d2d_sinr_random_2);% 在matlab中画图我们使用cdfplot,这个命令
set(h1,'color','b','LineWidth',2);

hold on;
 h2=cdfplot(d2d_sinr_rl);% 在matlab中画图我们使用cdfplot,这个命令
 set(h2,'color','r','LineWidth',2);

legend('random','reinforcement learning','Location','southeast');

xlabel('SINR');
ylabel('CDF');
title('D2D SINR CDF')

figure(2);
h3=cdfplot(d2d_rate_random_2);% 在matlab中画图我们使用cdfplot,这个命令
set(h3,'color','b','LineWidth',2);
hold on;
legend('random');

xlabel('RATE');
ylabel('CDF');
title('D2D RATE CDF')
