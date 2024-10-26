package programmers;

public class day2 {
	
	// 코딩테스트 입문
	// 1. 두 수의 나눗셈
	class Solution {
	    public int solution(int num1, int num2) {
	        double answer = (double)num1 / num2;
	        answer = answer * 1000;
	        return (int)answer;
	    }
	}
	
	// 2. 숫자 비교하기
	class Solution2 {
	    public int solution(int num1, int num2) {
	        if (num1 == num2) 
	            return 1;
	        else
	            return -1;
	    }
	}
	
	// 3. 분수의 덧셈
	// 어려움...
	
	// 4. 배열 두 배 만들
	

}
