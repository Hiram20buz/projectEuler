//Not finished yet
var fibonacci;
fibonacci = (function() {
  var fib, memo;
  memo = [0, 1];
  return fib = function(n) {
    var _ref;
    return (_ref = memo[n]) != null ? _ref : memo[n] = fib(n - 1) + fib(n - 2);
  };
})();
console.log(fibonacci(34));
if (fibonacci(34) <= 4000000){ console.log("true")}
else{console.log("false")}
