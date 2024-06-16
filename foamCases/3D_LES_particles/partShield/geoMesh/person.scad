translate([0,0,60])
    union() {

        difference() {
            
            union() {
                
                // shield
                difference() {
                    translate([0,35,-115])
                        cylinder(h=200, r1=110, r2=80); // front
                    translate([0,35,-120])
                        cylinder(h=220, r1=100, r2=70); // back
                }
                
                // connection
                translate([0,35,50])
                    linear_extrude(height=45) // recess ignored
                        resize([160,170])
                            circle(d=100);
            }
            
            // remove half of above volumes
            translate([-150,-365,-150])
                cube(400);  

        }

        // Dimensions: https://en.wikipedia.org/wiki/Human_head#Average_head_sizes 

        // head
        resize(newsize=[150, 200, 230])
            sphere(r=100);

        // nose
        translate([0,95,-39])
            rotate(a=[10,0,0])
                cylinder(h=45, r1=14, r2=5);
        
        // nostrils
        translate([6,100,-40])
            rotate(a=[0,0,40])
                linear_extrude(height=5)
                    resize([5, 10])
                        circle(d=10);
        translate([-6,100,-40])
            rotate(a=[0,0,-40])
                linear_extrude(height=5)
                    resize([5, 10])
                        circle(d=10); 
        
        // neck
        rotate([-20,0,0])
            translate([0,20,-200])
                linear_extrude(height=200)
                    resize([80,100])
                        circle(d=100);
        
        // body
        translate([-175,-120,-220])
            cube([350,170,75]);
        
        // fan
        translate([0,80,-200])
            linear_extrude(height=40)
                circle(d=40);
        translate([-10,-20,-190])
            cube([20,100,20]);
    }