// Skeleton structure for data collection script
async function collectTaskInventory() {
  // 1. Get all projects
  const projects = await fetchAllProjects();

  // 2. For each project, get all task data
  const allTasks = [];
  for (const project of projects) {
    const projectData = await fetchProjectWithData(project.id);
    allTasks.push(...projectData.tasks);
  }

  // 3. Process and categorize tasks
  const taskAnalysisData = {
    byContext: categorizeByTags(allTasks, [
      "1.@home",
      "1.@desktop",
      "1.@anywhere",
      "1.@errands",
    ]),
    byEffort: categorizeByTags(allTasks, ["2.high-effort", "2.low-effort"]),
    byTimeEstimate: categorizeByTags(allTasks, [
      "3.time-5m",
      "3.time-15m",
      "3.time-30m",
      "3.time-60m+",
    ]),
    byImpact: categorizeByTags(allTasks, ["4.high-impact"]),
    byAge: analyzeTaskAge(allTasks),
    byProject: groupByProject(allTasks, projects),
  };

  return taskAnalysisData;
}
