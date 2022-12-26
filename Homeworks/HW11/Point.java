import java.lang.Math;

public class Point {
  private int x;
  private int y;

  public Point(int x, int y) {
    this.x = x;
    this.y = y;
  }

  public static void main(String[] args) {

    Point p1 = new Point(2, 3);
    Point p2 = new Point(-3, 1);
    Point p3 = new Point(-2, -3);

    System.out.println("p1.equals(p2) = " + p1.equals(p2));
    System.out.println("p1.equals(p3) = " + p1.equals(p3));
    System.out.println("p1.equals(null) = " + p1.equals(null));
    System.out.println("p1.equals(p1) = " + p1.equals(p1));

  }

  @Override
  public boolean equals(Object other) {

    // reflexive
    if (other == this)
      return true;

    // non-null
    if (other == null)
      return false;

    // don't even bother! they have different types
    if (getClass() != other.getClass())
      return false;

    Point point = (Point) other; // why do we need this type cast?
    // we need to typecast to be able to access the attributes of the point other

    if (Math.sqrt(Math.pow(point.x, 2) + Math.pow(point.y, 2)) == Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2)))
      return true;

    return x == point.x && y == point.y;
  }

  @Override
  public int hashCode() {
    int varCodeX = x;
    int varCodeY = y;

    // inits hash with the var code for one of the fields

    int hash = varCodeX;

    // hash = <prime number> * hash + var_code;
    hash = 41 * hash + varCodeY;

    return hash;
  }

  @Override
  public String toString() {
    return "[" + x + ", " + y + "]";
  }

}