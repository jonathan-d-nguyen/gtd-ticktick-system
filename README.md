<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<!--
*** Thanks for checking out this TickTick GTD Task Analysis project.
*** If you have a suggestion that would make this better, please fork the repo
*** and create a pull request or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">TickTick GTD Task Analysis Pipeline</h3>

  <p align="center">
    A comprehensive data processing pipeline for analyzing TickTick CSV exports to identify high-impact tasks and assess productivity patterns using Getting Things Done (GTD) methodology. Normalizes non-standard TickTick CSV exports, categorizes tasks by impact dimensions, and provides actionable insights for task prioritization.
    <br />
    <a href="https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#1-about-the-project">About The Project</a>
      <ul>
        <li><a href="#11-gtd-system-context">GTD System Context</a></li>
        <li><a href="#12-built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#2-quick-start">Quick Start</a>
      <ul>
        <li><a href="#21-prerequisites">Prerequisites</a></li>
        <li><a href="#22-basic-setup">Basic Setup</a></li>
        <li><a href="#23-basic-usage">Basic Usage</a></li>
      </ul>
    </li>
    <li>
      <a href="#3-data-processing--analysis">Data Processing & Analysis</a>
      <ul>
        <li><a href="#31-csv-normalization">CSV Normalization</a></li>
        <li><a href="#32-task-matrix-analysis">Task Matrix Analysis</a></li>
        <li><a href="#33-high-impact-identification">High-Impact Identification</a></li>
        <li><a href="#34-advanced-filtering">Advanced Filtering</a></li>
        <li><a href="#35-export-formats">Export Formats</a></li>
      </ul>
    </li>
    <li><a href="#4-roadmap">Roadmap</a></li>
    <li>
      <a href="#5-contributing">Contributing</a>
      <ul>
        <li><a href="#51-top-contributors">Top Contributors</a></li>
      </ul>
    </li>
    <li><a href="#6-license">License</a></li>
    <li><a href="#7-contact">Contact</a></li>
    <li><a href="#8-acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- Back to top link template for use throughout document -->

<a id="readme-top"></a>

<!-- ABOUT THE PROJECT -->

## 1. About The Project

This project provides a comprehensive data processing pipeline for analyzing TickTick CSV exports to identify high-impact tasks and assess productivity patterns using Getting Things Done (GTD) methodology. The system normalizes non-standard TickTick CSV exports, categorizes tasks across five impact dimensions, and provides actionable insights for strategic task prioritization.

**Key Features:**

- **CSV Normalization**: Cleanses TickTick's non-standard CSV format with metadata headers and multiline fields
- **Task Matrix Analysis**: Generates comprehensive task counts by list, status, and priority
- **High-Impact Assessment**: Evaluates tasks across five GTD dimensions for strategic prioritization
- **Interactive Filtering**: Context-based task filtering with menu-driven selection
- **Pattern Recognition**: Identifies productivity patterns and optimization opportunities
- **Export Analytics**: Provides insights for continuous improvement of task management

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 1.1. GTD System Context

This project implements data analysis components of the **Getting Things Done (GTD)** productivity methodology created by David Allen. GTD is a personal productivity system that emphasizes capturing all tasks and ideas in an external system, then organizing and prioritizing them for systematic execution.

**Core GTD Principles Applied:**

- **Capture**: Process TickTick CSV exports containing all captured tasks
- **Clarify**: Normalize and categorize tasks by context, effort, and time requirements
- **Organize**: Structure tasks into Projects, Next Actions, and Someday/Maybe lists
- **Reflect**: Analyze task patterns and productivity metrics through data visualization
- **Engage**: Identify high-impact tasks for strategic focus using five-dimension assessment

**High-Impact Prioritization Framework:**

The system evaluates tasks across five critical dimensions:

1. **Financial Impact**: Tasks affecting financial situation (immediate and long-term)
2. **Career Growth**: Professional advancement, skills, networking, credentials
3. **Home Foundation**: Basic home functioning, safety, essential repairs
4. **Family Support**: Practical and emotional support for family members
5. **Mental Bandwidth**: Stress reduction, decision elimination, cognitive load management

**Tag System Implementation:**

- **Context Tags**: `1.@home`, `1.@desktop`, `1.@anywhere`, `1.@errands`
- **Effort Tags**: `2.high-effort`, `2.low-effort`
- **Time Tags**: `3.time-5m`, `3.time-15m`, `3.time-30m`, `3.time-60m+`
- **Impact Tags**: `4.high-impact`, `4.waiting`, `4.next-action`

This data analysis pipeline supports the systematic identification of high-leverage activities that create disproportionate positive outcomes across these five life dimensions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 1.2. Built With

- [![Python][Python.org]][Python-url]
- [![CSV][CSV Badge]][CSV-url]
- [![Pandas][Pandas Badge]][Pandas-url]
- [![TickTick][TickTick Badge]][TickTick-url]
- [![Git][Git Badge]][Git-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- QUICK START -->

## 2. Quick Start

Get up and running quickly with basic task analysis. For advanced features, see [Data Processing & Analysis](#3-data-processing--analysis).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 2.1. Prerequisites

1. **Python Requirements**

   ```sh
   # Python 3.6+ required
   python3 --version
   ```

2. **TickTick Export**

   - Export your TickTick data as CSV from TickTick web interface
   - Place CSV file in the project directory

3. **Optional: Virtual Environment**

   ```sh
   # Create virtual environment (recommended)
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 2.2. Basic Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis.git
   cd ticktick-gtd-analysis
   ```

2. **Add your TickTick CSV export**

   ```sh
   # Copy your TickTick export to the project directory
   cp ~/Downloads/TickTick-backup-2025-06-22.csv .
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 2.3. Basic Usage

1. **Normalize CSV export**

   ```sh
   # Normalize TickTick CSV format
   python3 csv-normalizer.py TickTick-backup-2025-06-22.csv
   ```

   Output example:
   ```
   Successfully normalized CSV file. Output saved to TickTick-backup-2025-06-22-normalized.csv
   
   Task Matrix by List Names:
   List Name                                     Uncompleted  Completed  Cancelled  Total
   ---------------------------------------------------------------------------
   Projects                                      23           45         2          70
   OneOff Tasks                                  15           32         1          48
   Waiting For                                   5            8          0          13
   ```

2. **Interactive task analysis**

   ```sh
   # Display task matrix with interactive filtering
   python3 display_columns-interactive.py --menu
   ```

3. **Quick analysis (default filters)**

   ```sh
   # Auto-analyze projects and oneoff tasks (uncompleted only)
   python3 display_columns-interactive.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DATA PROCESSING & ANALYSIS -->

## 3. Data Processing & Analysis

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 3.1. CSV Normalization

The `csv-normalizer.py` script handles TickTick's non-standard CSV format:

**TickTick CSV Issues Addressed:**
- Removes metadata header (lines 1-6)
- Preserves multiline fields with proper quoting
- Handles Unicode characters and special formatting
- Creates standard CSV structure for data analysis

**Usage:**

```sh
# Basic normalization
python3 csv-normalizer.py input.csv

# The script automatically:
# 1. Removes first 6 metadata lines
# 2. Preserves column headers (line 7)
# 3. Properly quotes multiline content fields
# 4. Outputs: input-normalized.csv
```

**Output Structure:**

```csv
"Folder Name","List Name","Task Title","Start Date","Tags","Content","Priority","Due Date","Status"
"GTD","Projects","Review quarterly goals","","4.high-impact","Assess progress...","5","2025-06-30","0"
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 3.2. Task Matrix Analysis

Generate comprehensive task statistics across all lists:

**Features:**
- Task counts by completion status (uncompleted, completed, cancelled)
- List-based organization
- Total task summaries
- Status distribution analysis

**Matrix Output Example:**

```
Task Matrix by List Names:
List Name                                     Uncompleted  Completed  Cancelled  Total
---------------------------------------------------------------------------
Projects                                      23           45         2          70
OneOff Tasks                                  15           32         1          48
Waiting For                                   5            8          0          13
Someday/Maybe                                 8            2          3          13
Reference                                     0            12         0          12
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 3.3. High-Impact Identification

The system supports identification of high-leverage tasks using GTD methodology:

**Five-Dimension Impact Assessment:**

1. **Financial Impact** (1-5 scale)
   - Immediate financial benefit
   - Long-term financial security
   - Passive income generation
   - Expense reduction

2. **Career Growth** (1-5 scale)
   - Skill development
   - Network expansion
   - Credential acquisition
   - Professional advancement

3. **Home Foundation** (1-5 scale)
   - Safety improvements
   - Essential repairs
   - Organization systems
   - Infrastructure upgrades

4. **Family Support** (1-5 scale)
   - Practical assistance
   - Emotional support
   - Educational support
   - Health and wellness

5. **Mental Bandwidth** (1-5 scale)
   - Stress reduction
   - Decision elimination
   - Process automation
   - Cognitive load reduction

**Usage in Analysis:**

Tasks tagged with `4.high-impact` in TickTick are automatically highlighted in the analysis output for strategic focus during daily and weekly reviews.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 3.4. Advanced Filtering

The `display_columns-interactive.py` script provides comprehensive filtering options:

**Interactive Mode:**

```sh
python3 display_columns-interactive.py --menu
```

**Menu Features:**
- CSV file selection (most recent first)
- Multi-list selection (Projects, OneOff Tasks, etc.)
- Status filtering (uncompleted, completed, cancelled)
- Combined criteria filtering

**Default Mode (Automated):**

```sh
python3 display_columns-interactive.py
```

**Default Filters:**
- Lists: Folder contains 'projects' OR list contains 'oneoff'
- Status: Uncompleted only
- Auto-selects most recent CSV file

**Output Columns:**

```
Filtered Tasks:
Task Title                               Folder    List         Tags         Priority   Content
Review quarterly objectives              GTD       Projects     4.high-impact High      Assess progress against Q2 goals...
Update project documentation            Work      OneOff Tasks 2.low-effort  Medium     Document recent changes to...
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 3.5. Export Formats

**Generated Files:**

1. **Normalized CSV**: `input-normalized.csv`
   - Standard CSV format
   - Ready for data analysis tools
   - Preserves all original data

2. **Task Matrix**: Console output
   - Summary statistics by list
   - Status distribution
   - Total counts

3. **Filtered Tasks**: Console output
   - Task details with key metadata
   - Priority indicators
   - Content previews (first 100 characters)

**Integration with Analysis Tools:**

The normalized CSV files can be imported into:
- Excel/Google Sheets for pivot tables
- Tableau/Power BI for advanced visualization
- Pandas/R for statistical analysis
- Database systems for complex queries

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## 4. Roadmap

- [ ] **Enhanced Impact Analysis**

  - [ ] Five-dimension scoring automation
  - [ ] Confidence assessment integration
  - [ ] Task recommendation engine
  - [ ] Priority optimization algorithms

- [ ] **Advanced Visualization**

  - [ ] Task hierarchy tree (Parent/Child relationships)
  - [ ] Productivity trend analysis
  - [ ] Completion rate dashboards
  - [ ] Time-based pattern recognition

- [ ] **API Integration**

  - [ ] Real-time TickTick API connectivity
  - [ ] Live task analysis dashboard
  - [ ] Automated data collection
  - [ ] Historical trend analysis

- [ ] **Export Enhancements**

  - [ ] PDF report generation
  - [ ] Excel template integration
  - [ ] JSON export format
  - [ ] Database export options

- [x] **Core Pipeline**

  - [x] CSV normalization with multiline field support
  - [x] Task matrix generation by list and status
  - [x] Interactive filtering system
  - [x] Default filter automation for GTD workflows
  - [x] Priority and tag analysis
  - [x] Content preview and metadata display

- [x] **GTD Integration**
  - [x] Context-based task categorization
  - [x] High-impact task identification
  - [x] Project vs. single-action distinction
  - [x] Status-based filtering (uncompleted, completed, cancelled)

See the [open issues](https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 5. Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Test with sample TickTick CSV data
4. Update documentation as needed
5. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the Branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

### Testing Guidelines

- Test with various TickTick CSV export formats
- Verify Unicode and special character handling
- Ensure multiline content preservation
- Validate output CSV format compliance
- Test interactive menu functionality

### Data Privacy

When contributing:
- Use anonymized or example data only
- Do not include personal task content
- Exclude real TickTick exports from commits
- Use `*-example.csv` naming for sample files

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 5.1. Top contributors:

<a href="https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jonathan-d-nguyen/ticktick-gtd-analysis" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 6. License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## 7. Contact

Jonathan Nguyen - jonathan@jdnguyen.tech

Project Link: [https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis](https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## 8. Acknowledgments

- [David Allen](https://gettingthingsdone.com/) - Creator of the Getting Things Done methodology
- [TickTick](https://ticktick.com/) - For the task management platform and CSV export functionality
- [Awesome README Template](https://github.com/othneildrew/Best-README-Template/) - For the documentation structure
- [Python CSV Module](https://docs.python.org/3/library/csv.html) - For robust CSV processing capabilities
- [GTD Community](https://gettingthingsdone.com/community/) - For productivity methodology insights and best practices

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/jonathan-d-nguyen/ticktick-gtd-analysis.svg?style=for-the-badge
[contributors-url]: https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jonathan-d-nguyen/ticktick-gtd-analysis.svg?style=for-the-badge
[forks-url]: https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis/network/members
[stars-shield]: https://img.shields.io/github/stars/jonathan-d-nguyen/ticktick-gtd-analysis.svg?style=for-the-badge
[stars-url]: https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis/stargazers
[issues-shield]: https://img.shields.io/github/issues/jonathan-d-nguyen/ticktick-gtd-analysis.svg?style=for-the-badge
[issues-url]: https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis/issues
[license-shield]: https://img.shields.io/github/license/jonathan-d-nguyen/ticktick-gtd-analysis.svg?style=for-the-badge
[license-url]: https://github.com/jonathan-d-nguyen/ticktick-gtd-analysis/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/JonathanDanhNguyen
[product-screenshot]: images/screenshot.png
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[CSV Badge]: https://img.shields.io/badge/CSV-Processing-green?style=for-the-badge&logo=file-text&logoColor=white
[CSV-url]: https://docs.python.org/3/library/csv.html
[Pandas Badge]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[TickTick Badge]: https://img.shields.io/badge/TickTick-Task%20Management-blue?style=for-the-badge&logo=check-square&logoColor=white
[TickTick-url]: https://ticktick.com/
[Git Badge]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com/
