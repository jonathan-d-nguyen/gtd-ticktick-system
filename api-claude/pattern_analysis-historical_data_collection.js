async function collectHistoricalPatterns(daysBack = 30) {
  // Set date range
  const endDate = new Date();
  const startDate = new Date();
  startDate.setDate(startDate.getDate() - daysBack);

  // Collect completed tasks in date range
  const completedTasks = await fetchCompletedTasks(startDate, endDate);

  // Analyze patterns
  return {
    completionRates: calculateCompletionRates(completedTasks),
    contextEffectiveness: analyzeCompletionByContext(completedTasks),
    effortCorrelation: analyzeCompletionByEffort(completedTasks),
    timeEstimateAccuracy: analyzeTimeEstimates(completedTasks),
  };
}
