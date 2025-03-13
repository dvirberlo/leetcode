class Solution {
    static class Reverser {
        StringBuilder str;

        public Reverser(String s) {
            str = new StringBuilder(s);
        }

        public String reverse() {
            this.deleteSpaces(0, 0);
            this.str.reverse();
            this.deleteSpaces(0, 0);
            this.trimWords();
            this.reverseWords();
            return this.str.toString();
        }

        private void trimWords() {
            int i = 0;
            while (i < str.length()) {
                while (i < str.length() && str.charAt(i) != ' ')
                    i++;
                i = deleteSpaces(i, 1);
            }
        }

        private int deleteSpaces(int index, int keep) {
            int start = index, end = index;
            while (end < str.length() && str.charAt(end) == ' ')
                end++;
            if (start + keep <= end)
                str.delete(start + keep, end);
            return start + keep;
        }

        private void reverseWords() {
            int start = 0, end = 0;
            while (start < str.length()) {
                while (end < str.length() && str.charAt(end) != ' ')
                    end++;
                this.reverseSub(start, end);
                start = end = end + 1;
            }
        }

        private void reverseSub(int start, int stop) {
            for (int i = 0; i < (stop - start) / 2; i++) {
                char a = this.str.charAt(start + i);
                char b = this.str.charAt(stop - 1 - i);
                this.str.setCharAt(start + i, b);
                this.str.setCharAt(stop - 1 - i, a);
            }
        }
    }

    public String reverseWords(String s) {
        Reverser r = new Reverser(s);
        return r.reverse();
    }
}