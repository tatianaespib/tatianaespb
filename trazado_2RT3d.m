clc
clear all


x=-5.0*100:.1*100:10.0*100;
[X,Y] = meshgrid(x);
a=0; b=0; c=1; d0=0.0; d1=-5.0; d2=-10.0; d3=-15.0; d4=-20.0; d5=-30.0; d6=-40.0; d7=-50.0;d8=-60.0; 
d9=-70; d10=-80;  d11=-100; d12=-120.0; d13=-150.0; d14=-200.0;

Z0=(d0- a * X - b * Y)/c;
Z1=(d1- a * X - b * Y)/c;
Z2=(d2- a * X - b * Y)/c;
Z3=(d3- a * X - b * Y)/c;
Z4=(d4- a * X - b * Y)/c;
Z5=(d5- a * X - b * Y)/c;
Z6=(d6- a * X - b * Y)/c;
Z7=(d7- a * X - b * Y)/c;
Z8=(d8- a * X - b * Y)/c;
Z9=(d9- a * X - b * Y)/c;
Z10=(d10- a * X - b * Y)/c;
Z11=(d11- a * X - b * Y)/c;
Z12=(d12- a * X - b * Y)/c;%500-((X-500)/50)^2+((Y-400)/50)^2;%;
Z13=(d13- a * X - b * Y)/c;
Z14=(d14- a * X - b * Y)/c;

%line([0.3 0.4],[.8 0.9],[-2.9 -1.0],'color','r','linewidth',2);
hold on 

% Z=-2.0
surf(X,Y,Z0)
hold on
surf(X,Y,Z1)
hold on
surf(X,Y,Z2)
hold on
surf(X,Y,Z3)
hold on
surf(X,Y,Z4)
hold on
surf(X,Y,Z5)
hold on
surf(X,Y,Z6)
hold on
surf(X,Y,Z7)
hold on
surf(X,Y,Z8)
hold on
surf(X,Y,Z9)
hold on
surf(X,Y,Z10)
hold on
surf(X,Y,Z11)
hold on
surf(X,Y,Z12)
hold on
surf(X,Y,Z13)
hold on
surf(X,Y,Z14)
hold on
colormap()
box on 
% BoxPlot3(8, 11, -90, 100, 100, -100)
shading flat
xlabel('x'); ylabel('y'); zlabel('z')
grid on 
lat=[6.191 6.54 7.429 6.436 8.862 5.893 5.564 5.224 4.63 4.84 4.199 7.34 8.24 7.107];
lon=[-75.529 -74.456 -74.858 -71.791 -73.992 -73.083   -74.072 -74.869 -75.365 -73.732 -74.32 -72.134 -72.7 -73.319];
XX=[ 441475.751  560143.16  515669.301 191256.041 610840.452 712233.331 602768.917 514508.81 459551.947 640650.695  575400.715 818195.891  753915.465 685160.528 642239.963];
YY=[ 684347.33 722930.463  821176.275 712244.763 979745.55 651741.205   624818.098 615010.158   577436.729  511890.928 535015.934 464707.073 811986.322 911219.744 785775.196]; 

xx2=XX./1000;
yy2=YY./1000;

plot(xx2,yy2,'k*','linewidth',10)

t=0:0.01:1;
theta1_min=5;
theta1_max=360
d_theta1=20;
phi_min=5;
phi_max=180;
d_phi=30;
%velocidades
v_6=5.2;
v_5=4.9;
v_4=4.3;
v_3=3.9;
v_2=2.5;
v_1=1.2;
v_0=0.9;
v_7=6.2;
v_8=7.9;
v_9=8.3;
v_10=8.9;
v_11=9.5;
v_12=10.2;
v_13=10.9;
v_14=11.5;




x_0=0.5*100;
y_0=0.5*100;
z_0=-200;
% gtext('Est')
% [X,Y]=ginput(1)
X=37.1212;
Y=61.3419

P_0=[x_0 y_0 z_0];
plot3(x_0,y_0,z_0)
k=0
for phi = phi_min:d_phi:phi_max;
    for theta = theta1_min:d_theta1:theta1_max;
        dri=[sin(phi*pi/180)*cos(theta*pi/180),sin(theta*pi/180)*sin(phi*pi/180),cos(phi*pi/180)];
        dr=abs([dri(1)*100,dri(2)*100,d4]);

%%%primer rayo 
        line([dr(1), x_0],[dr(2) y_0],[d13,d14],'color','k','linewidth',1.2)
        phi_r=asin((v_12/v_13)*sin(phi*pi/180));  %%Snell%
        N1=[dr(1)-dri(1) dr(2)-dri(2) d13-d14];
        %Normal
        %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v1=cross(dr,N1);
        ang=atan((v1(2)/v1(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
        %%%%%% Segundo Rayo
        dr2=abs([sin(phi_r*pi/180)*cos(ang*pi/180)+2*dr(1),sin(phi_r*pi/180)*sin(ang*pi/180)+2*dr(2),cos(phi_r*pi/180)]);
        dr22=[dr2(1),dr2(2),d12];
        line([dr(1) dr2(1)], [dr(2) dr2(2)],[d13 d12],'color','k','linewidth',1.2)
%         
%         
        phi_r3=asin((v_11/v_12)*sin(phi_r*pi/180));  %%Snell%
        N2=[dr2(1)-dr2(1) dr2(2)-dr2(2) d11-d12];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v3=cross(dr2,N2);
        ang3=atan((v3(2)/v3(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% Tercer Rayo
        dr3=abs([sin(phi_r3*pi/180)*cos(ang3*pi/180)+1.4*dr2(1),sin(phi_r*pi/180)*sin(ang3*pi/180)+1.4*dr2(2),cos(phi_r3*pi/180)]);
        line([dr2(1) dr3(1)],[dr2(2) dr3(2)],[d12 d11],'color','k','linewidth',1.2)
        dr33=[dr3(1), dr3(2), d11];
        
        phi_r4=asin((v_10/v_11)*sin(phi_r*pi/180));  %%Snell%
        N3=[dr3(1)-dr3(1) dr3(2)-dr3(2) d11-d10];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v4=cross(dr2,N3);
        ang4=atan((v4(2)/v4(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 4 Rayo
        dr4=abs([sin(phi_r4*pi/180)*cos(ang4*pi/180)+1.1*dr3(1),sin(phi_r4*pi/180)*sin(ang4*pi/180)+1.1*dr3(2),cos(phi_r4*pi/180)]);
        line([dr3(1) dr4(1)],[dr3(2) dr4(2)],[d11 d10],'color','k','linewidth',1.2)
        dr44=[dr4(1), dr4(2), d10];
        
        phi_r5=asin((v_9/v_10)*sin(phi_r*pi/180));  %%Snell%
        N4=[dr3(1)-dr3(1) dr3(2)-dr3(2) d11-d10];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v5=cross(dr4,N4);
        ang5=atan((v5(2)/v5(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 5 Rayo
        dr5=abs([sin(phi_r5*pi/180)*cos(ang5*pi/180)+1.1*dr4(1),sin(phi_r5*pi/180)*sin(ang5*pi/180)+1.1*dr4(2),cos(phi_r5*pi/180)]);
        line([dr4(1) dr5(1)],[dr4(2) dr5(2)],[d10 d9],'color','k','linewidth',1.2)
        dr55=[dr5(1), dr5(2), d9];
        
        
        phi_r6=asin((v_8/v_9)*sin(phi_r*pi/180));  %%Snell%
        N5=[dr4(1)-dr4(1) dr4(2)-dr4(2) d9-d8];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v6=cross(dr5,N5);
        ang7=atan((v6(2)/v6(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 6 Rayo
        dr6=abs([sin(phi_r6*pi/180)*cos(ang7*pi/180)+1.2*dr5(1),sin(phi_r6*pi/180)*sin(ang7*pi/180)+1.2*dr5(2),cos(phi_r6*pi/180)]);
        line([dr5(1) dr6(1)],[dr5(2) dr6(2)],[d9 d8],'color','k','linewidth',1.2)
        dr66=[dr6(1), dr6(2), d8];
        
        
        phi_r7=asin((v_7/v_8)*sin(phi_r*pi/180));  %%Snell%
        N6=[dr5(1)-dr5(1) dr5(2)-dr5(2) d7-d8];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v7=cross(dr6,N6);
        ang7=atan((v7(2)/v7(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 7 Rayo
        dr7=abs([sin(phi_r7*pi/180)*cos(ang7*pi/180)+1.1*dr6(1),sin(phi_r*pi/180)*sin(ang7*pi/180)+1.1*dr6(2),cos(phi_r7*pi/180)]);
        line([dr6(1) dr7(1)],[dr6(2) dr7(2)],[d8 d7],'color','k','linewidth',1.2)
        dr77=[dr7(1), dr7(2), d7];
        
        phi_r8=asin((v_6/v_7)*sin(phi_r*pi/180));  %%Snell%
        N7=[dr6(1)-dr6(1) dr6(2)-dr6(2) d6-d7];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v8=cross(dr7,N7);
        ang8=atan((v8(2)/v8(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 8 Rayo
        dr8=abs([sin(phi_r8*pi/180)*cos(ang8*pi/180)+1.1*dr7(1),sin(phi_r8*pi/180)*sin(ang8*pi/180)+1.1*dr7(2),cos(phi_r8*pi/180)]);
        line([dr7(1) dr8(1)],[dr7(2) dr8(2)],[d7 d6],'color','k','linewidth',1.2)
        dr88=[dr8(1), dr8(2), d6];
        
        phi_r9=asin((v_5/v_6)*sin(phi_r*pi/180));  %%Snell%
        N8=[dr7(1)-dr7(1) dr7(2)-dr7(2) d7-d8];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v9=cross(dr8,N8);
        ang9=atan((v9(2)/v9(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 9 Rayo
        dr9=abs([sin(phi_r9*pi/180)*cos(ang9*pi/180)+1.1*dr8(1),sin(phi_r9*pi/180)*sin(ang9*pi/180)+1.1*dr8(2),cos(phi_r9*pi/180)]);
        line([dr8(1) dr9(1)],[dr8(2) dr9(2)],[d6 d5],'color','k','linewidth',1.2)
        dr99=[dr9(1), dr9(2), d5];
        
        phi_r10=asin((v_4/v_5)*sin(phi_r*pi/180));  %%Snell%
        N9=[dr8(1)-dr8(1) dr8(2)-dr8(2) d6-d7];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v10=cross(dr9,N9);
        ang10=atan((v10(2)/v10(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 10 Rayo
        dr10=abs([sin(phi_r10*pi/180)*cos(ang10*pi/180)+1.1*dr9(1),sin(phi_r10*pi/180)*sin(ang10*pi/180)+1.1*dr9(2),cos(phi_r10*pi/180)]);
        line([dr9(1) dr10(1)],[dr9(2) dr10(2)],[d5 d4],'color','k','linewidth',1.2)
        dr100=[dr10(1), dr10(2), d4];
        
        phi_r11=asin((v_3/v_4)*sin(phi_r*pi/180));  %%Snell%
        N10=[dr9(1)-dr9(1) dr9(2)-dr9(2) d5-d6];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v11=cross(dr10,N10);
        ang11=atan((v11(2)/v11(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 10 Rayo
        dr11=abs([sin(phi_r11*pi/180)*cos(ang11*pi/180)+1.1*dr10(1),sin(phi_r11*pi/180)*sin(ang11*pi/180)+1.1*dr10(2),cos(phi_r11*pi/180)]);
        line([dr10(1) dr11(1)],[dr10(2) dr11(2)],[d4 d3],'color','k','linewidth',1.2)
        dr111=[dr11(1), dr11(2), d3];
        
        phi_r12=asin((v_2/v_3)*sin(phi_r*pi/180));  %%Snell%
        N10=[dr9(1)-dr9(1) dr9(2)-dr9(2) d5-d6];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v12=cross(dr10,N10);
        ang12=atan((v12(2)/v12(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 10 Rayo
        dr12=abs([sin(phi_r12*pi/180)*cos(ang12*pi/180)+1.1*dr11(1),sin(phi_r12*pi/180)*sin(ang12*pi/180)+1.1*dr11(2),cos(phi_r12*pi/180)]);
        line([dr11(1) dr12(1)],[dr11(2) dr12(2)],[d3 d2],'color','k','linewidth',1.2)
        dr122=[dr12(1), dr12(2), d2];
        
        phi_r13=asin((v_1/v_2)*sin(phi_r*pi/180));  %%Snell%
        N11=[dr10(1)-dr10(1) dr10(2)-dr10(2) d4-d5];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v13=cross(dr11,N11);
        ang13=atan((v13(2)/v13(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 10 Rayo
        dr13=abs([sin(phi_r13*pi/180)*cos(ang13*pi/180)+1.1*dr12(1),sin(phi_r13*pi/180)*sin(ang13*pi/180)+1.1*dr12(2),cos(phi_r13*pi/180)]);
        line([dr12(1) dr13(1)],[dr12(2) dr13(2)],[d2 d1],'color','k','linewidth',1.2)
        dr133=[dr12(1), dr12(2), d2];
        
        phi_r14=asin((v_0/v_1)*sin(phi_r*pi/180));  %%Snell%
        N12=[dr11(1)-dr11(1) dr11(2)-dr11(2) d3-d4];
%          %Normal
         %line([dr(1) dr(1)],[dr(2) dr(2)],[-2 dr(3)],'color','r','linewidth',2)
        v14=cross(dr12,N12);
        ang14=atan((v14(2)/v14(1))*pi/180);%/180cos(phi_r)-phi_r)/cos(phi)%atan((v1(2)/v1(1))*pi/180);
%         %%%%%% 10 Rayo
        dr14=abs([sin(phi_r14*pi/180)*cos(ang14*pi/180)+1.1*dr13(1),sin(phi_r14*pi/180)*sin(ang14*pi/180)+1.1*dr13(2),cos(phi_r14*pi/180)]);
        line([dr13(1) dr14(1)],[dr13(2) dr14(2)],[d1 d0],'color','k','linewidth',1.2)
        dr133=[dr13(1), dr13(2), d1];    
        
        tol=5.0;
        dist=sqrt((X-dr3(1))^2+(Y-dr3(2))^2);
        
        if dist<tol
            k=k+1;
            
            line([x_0 dr(1)],[y_0 dr(2)],[d5 d4],'color','k','linewidth',1.2)
            line([dr(1) dr2(1)], [dr(2) dr2(2)],[d4 d2],'color','k','linewidth',1.2)
            line([dr2(1) dr3(1)],[dr2(2) dr3(2)],[d2 d0],'color','k','linewidth',1.2)
            fprintf('distancia theta phi \n %3.2f %3.2f %3.2f \n',dist,theta,phi)
%             fprintf('angulo theta: \n %3.2f\n',theta)
%             fprintf('angulo phi: \n %3.2f\n',phi)
            p1=sqrt((P_0(1)-dr(1))^2+(P_0(2)-dr(2))^2+(P_0(3)-dr(3))^2);
            p2=sqrt((dr22(1)-dr(1))^2+(dr22(2)-dr(2))^2+(dr22(3)-dr(3))^2);
            p3=sqrt((dr33(1)-dr22(1))^2+(dr22(2)-dr33(2))^2+(dr22(3)-dr33(3))^2);
            t1=p1/v_6;
            t2=p2/v_4;
            t3=p3/v_2;
            Tt=t1+t2+t3;
            fprintf('tiempo total: \n %3.2f\n',Tt)
        end
       
        
    end


end



