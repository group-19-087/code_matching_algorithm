class Person {
    public Person() {
        System.out.println("Person default 
        constructor");    
    }

    public Person(int para1 ) {
        System.out.println("Person overloaded 
        constructor");   
    }

}

class Student extends Person {
    public Student() {
        System.out.println("Student default 
        constructor");
    }
    public Student(int para1, int para2 ) {
        super(para1);
        System.out.println("Student overloaded 
        constructor");
    }
    
}

class PostGraduate extends Student {
    public PostGraduate() {
        System.out.println("Postgraduate 
        default constructor");
    }
    public PostGraduate(int para1, int para2,
    int para3 ) {
        super(para1, para2);
        System.out.println("Postgraduate 
        overloaded constructor");
    }
}

class Main {
    public static void main(String[] args) {
        PostGraduate p = new PostGraduate(1, 2, 3 );
    }
}