union() {

    difference() {
        
        union() {
        
            difference() {
                // shield front
                translate([0,0,-50])
                    linear_extrude(height=150)
                        resize([170,200])
                            circle(d=100);
                
                // shield back
                translate([0,0,-200])
                    linear_extrude(height=400)
                        resize([163,193])
                            circle(d=50);
            }
            
            // connection
            translate([0,0,65])
                linear_extrude(height=35) // make connection flush with top of shield (not recessed down)
                    resize([163,193])
                        circle(d=100);
        }
        
        // remove half of entities above
        translate([-150,-300,-150])
            cube(300);  

    }

    // head
    translate([0,-20,40])
        resize(newsize=[140,180,200]) 
            sphere(r=100);
    
    // neck
    rotate([-20,0,0])
        translate([0,-15,-150])
            linear_extrude(height=200)
                resize([90,100])
                    circle(d=100);
    
    // body
    translate([-175,-150,-175])
        cube([350,170, 75]);
}