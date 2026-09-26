import java.util.*;
public class RouteOptimizer{
 record Bin(String id,double fill,double distanceKm){}
 static double priority(Bin b){return b.fill*.75+(20/Math.max(b.distanceKm,.5))*.25;}
 public static void main(String[] args){
  List<Bin> bins=new ArrayList<>(List.of(new Bin("SW-204",94,2.4),new Bin("SW-118",81,4.2),new Bin("SW-077",67,3.1),new Bin("SW-311",46,6.5)));
  bins.sort(Comparator.comparingDouble(RouteOptimizer::priority).reversed());
  System.out.println("EcoGrid Java Route Optimizer");
  for(Bin b:bins)System.out.printf("%s | fill=%.1f%% | distance=%.1f km | priority=%.1f%n",b.id(),b.fill(),b.distanceKm(),priority(b));
 }
}