public class LetterGrade{
    public static void main(String[] args){
        double score = 87.5;
        char letterGrade;

        letterGrade = calcGrade(score);
        System.out.println("Your grade is " + letterGrade);
    }

    public static char calcGrade(double numericScore){
        if (numericScore >= 90.0){
            return 'A';
        }
        else if (numericScore >= 80.0){
            return 'B';
        }
        else if (numericScore >= 70.0){
            return 'C';
        }
        else if (numericScore >= 60.0){
            return 'D';
        }
        else {
            return 'F';
        }
    }
}