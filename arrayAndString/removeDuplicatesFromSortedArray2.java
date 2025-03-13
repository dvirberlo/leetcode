class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length < 1) return 0;
        Deduplicator d = new Deduplicator(nums, 2);
        int l = d.deduplicateAll();
        return l;
    }

    static class Deduplicator {
        int[] arr;
        int maxDup;
        private int i, k, currentDup, prev;
        public Deduplicator(int[] arr, int maxDup) {
            if (arr.length < 1) throw new RuntimeException("must pass non empty array");
            this.arr = arr;
            this.maxDup = maxDup;

            this.i = 0;
            this. k = 0;
            this.currentDup = 0;
            this.prev = -(arr[0] + 1);
        }

        boolean hasNext(){
            return this.i < this.arr.length;
        }

        int deduplicateAll(){
            while(this.hasNext()) this.deduplicate();
            return k;
        }

        void deduplicate() {
            if (!this.hasNext()) throw new RuntimeException("nothing left to deduplicate");
            int current = this.arr[i];
            if (current != this.prev || this.currentDup < this.maxDup) {
                arr[k] = current;
                this.currentDup++;
                if(current != this.prev) this.currentDup = 1;
                this.prev = current;
                this.k++;
            }
            i++;
        }
    }
}