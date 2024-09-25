function calculateOptimizedCoverage(intervals, arr) {
  const coverageMap = new Set(intervals);

  // 计算覆盖的元素
  let coveredCount = 0;
  for (const num of arr) {
    if (coverageMap.has(num)) {
      coveredCount++;
    }
  }

  console.log(coveredCount);
  console.log(intervals.length);
  return coveredCount / intervals.length; // 返回覆盖率
}

// 示例输入
// 生成大数据测试性能
//const C = [2, 4, 5, 13, 14, 15, 16, 17, 18, 25……
const C = Array.from({ length: 10000 }, (v, k) => k).filter(
  (v) =>
    v % 10 === 2 ||
    v % 10 === 4 ||
    v % 10 === 5 ||
    v % 10 === 3 ||
    v % 10 === 8 ||
    v % 10 === 7 ||
    v % 10 === 6 ||
    v % 10 === 1 ||
    v % 10 === 9
);
// const D = [1, 2, 4, 11, 12, 13, 14, 15……
const D = Array.from({ length: 10000 }, (v, k) => k).filter(
  (v) => v % 10 === 1 || v % 30 === 4 || v % 10 === 3
);

// 计算并输出覆盖率
var start = new Date().getTime()
const coverage2 = calculateOptimizedCoverage(C, D);
console.log(coverage2);

var end = new Date().getTime()
console.log('cost is', `${end - start}ms`)
