clc
clear

n=1000000;%要读入的行数
 
fid=fopen('d2d snr\d2d_sinr_random 10000.txt'); 
for i=1:n
    d2d_sinr_graph(i)=str2double(fgets(fid));
end 
fclose(fid);

fid=fopen('d2d_sinr_random.txt'); 
for i=1:n
    d2d_sinr_random(i)=str2double(fgets(fid));
end 
fclose(fid);

figure(1);
h1=cdfplot(d2d_sinr_graph);% 在matlab中画图我们使用cdfplot,这个命令
set(h1,'color','r','LineWidth',2);
hold on;

h2=cdfplot(d2d_sinr_random);% 在matlab中画图我们使用cdfplot,这个命令
set(h2,'color','b','LineWidth',2);

legend('graph-based','random','Location','southeast');


xlabel('SINR');
ylabel('CDF');
title('D2D SINR CDF')

