<!-- =========================================================================================
                                     HEADER SECTION
     ========================================================================================= -->
<div align="center">
  
  # Distributed Computing & Lab

  ### CSC802 · CSL802 · Semester VIII · Computer Engineering

  [![Curated by](https://img.shields.io/badge/Curated%20by-Amey%20Thakur-blue.svg)](https://github.com/Amey-Thakur)
  [![Syllabus](https://img.shields.io/badge/Syllabus-View-yellowgreen.svg)](MU%20SEM%20VIII%20SYLLABUS.pdf)
  [![Language](https://img.shields.io/badge/Language-Python%20%7C%20Java-blueviolet.svg)](./)
  [![Tech Stack](https://img.shields.io/badge/Tech%20Stack-Pyro4%20%7C%20RMI%20%7C%20RPC-orange.svg)](./)
  [![Type](https://img.shields.io/badge/Type-Theory%20%7C%20Laboratory-brightgreen.svg)](./)

  **A comprehensive collection of study materials and laboratory implementations for Distributed Computing, covering clock synchronization, election algorithms, deadlock detection, and load balancing.**

  ---

  [The Wall](#the-wall) &nbsp;·&nbsp; [Learning Path](#learning-path) &nbsp;·&nbsp; [Laboratory](#distributed-computing-laboratory) &nbsp;·&nbsp; [RPP](#research-paper-presentation) &nbsp;·&nbsp; [Quizzes](#quizzes) &nbsp;·&nbsp; [IAT](#iat---1) &nbsp;·&nbsp; [Exam](#semester-exam) &nbsp;·&nbsp; [Report](#submission-report)

</div>

---

> [!NOTE]
> **Reference Materials**: This repository includes a curated selection of textbooks and reference materials essential for mastering Distributed Computing concepts. Access them here: [Reference Books](Reference%20Books).

> [!TIP]
> **Distributed Systems Development**: When implementing distributed algorithms, always consider the impact of network latency and partial failures. Using idempotent operations and robust error handling is critical for building resilient distributed systems.

> [!WARNING]
> **COVID-19 Impact**: This coursework was completed during the COVID-19 pandemic in 2022. Due to the nationwide lockdown, several planned laboratory sessions and collaborative activities were adapted for remote learning. Despite these challenges, efforts were made to preserve the integrity and depth of all implementations.

---

<!-- =========================================================================================
                                     THE WALL SECTION
     ========================================================================================= -->
## THE WALL

<div align="center">

**Collaborative Study Notes by Amey & Mega**

<table>
<tr>
<td align="center">
<a href="https://github.com/Amey-Thakur">
<img src="https://github.com/Amey-Thakur.png" alt="Amey Thakur" width="150" height="150"/><br/>
<b>Amey Thakur</b>
</a>
</td>
<td align="center">
<a href="https://github.com/msatmod">
<img src="THE%20WALL/Mega/Mega.png" alt="Mega Satish" width="150" height="150"/><br/>
<b>Mega Satish</b>
</a>
</td>
</tr>
</table>

</div>

> [!IMPORTANT]
> 💝 **Special Thanks**: A heartfelt thank you to Mega for her constant support, patience, and clarity throughout this journey. Learning alongside her made a real difference, not only because she explained concepts so clearly, but because she truly cared about understanding them together. Her thoughtful approach turned challenges into meaningful learning moments.

### Laboratory Documentation - Notes Authored by [MEGA SATISH](https://github.com/msatmod)

| Module | Resource | Topics Covered |
|:---:|:---|:---|
| 4 | [DC Module - 4](THE%20WALL/DC_Module_4.pdf) | Consistency and Replication |
| 5 | [DC Module - 5](THE%20WALL/DC_Module_5.pdf) | Fault Tolerance and Recovery |
| 6 | [DC Module - 6](THE%20WALL/DC_Module_6.pdf) | Distributed File Systems and Security |

---

<!-- =========================================================================================
                                     LEARNING PATH SECTION
     ========================================================================================= -->
## Learning Path

### Phase 1: Communication & Synchronization
Foundational concepts of inter-process communication and logical clock synchronization.
- **Experiment-2**: Implement basic Socket Programming for client-server communication.
- **Experiment-3**: Develop a Calculator application using RMI/Pyro4.
- **Experiment-4**: Implement Lamport's Logical Clock for ordering events in a distributed system.

### Phase 2: Distributed Coordination
Implementing algorithms for election, mutual exclusion, and deadlock detection.
- **Experiment-5**: Implement the Bully Election Algorithm.
- **Experiment-6**: Implement the Token Ring Algorithm for mutual exclusion.
- **Experiment-7**: Implement the Chandy-Misra-Haas Algorithm for edge-chasing deadlock detection.

### Phase 3: Resource Management & Naming
Advanced topics in load balancing and name resolution services.
- **Experiment-8**: Implement Load Balancing algorithms in Java and Python.
- **Experiment-10**: Implement Name Resolution services and RPC-based communication.

---

<!-- =========================================================================================
                                     LABORATORY SECTION
     ========================================================================================= -->
## Distributed Computing Laboratory

### Experiment-1: Communication Paradigms
Introduction to distributed communication models.

| # | Program | Description | Report |
|:-:|:---|:---|:-:|
| — | Lab Report (PDF) | Detailed experiment report | [View](Distributed%20Computing%20Lab/Experiment-1/AMEY_B-50_DCL_EXPERIMENT-1.pdf) |

---

### Experiment-2: Socket Programming
Implementation of a basic Chat Application using Socket Programming.

| # | Program | Description | Source Code | Report |
|:-:|:---|:---|:-:|:-:|
| 1 | server.py | Chat server implementation | [View](Distributed%20Computing%20Lab/Experiment-2/server.py) | [View](Distributed%20Computing%20Lab/Experiment-2/AMEY_B-50_DCL_EXPERIMENT-2.pdf) |
| 2 | client.py | Chat client implementation | [View](Distributed%20Computing%20Lab/Experiment-2/client.py) | — |
| — | Kaggle | Interactive notebook | [Explore](https://www.kaggle.com/ameythakur20/chat-application-socket-programming) | — |

---

### Experiment-3: RMI / Pyro4
Implementation of a Calculator Application using Remote Method Invocation.

| # | Program | Description | Source Code | Report |
|:-:|:---|:---|:-:|:-:|
| 1 | server.py | RMI server implementation | [View](Distributed%20Computing%20Lab/Experiment-3/server.py) | [View](Distributed%20Computing%20Lab/Experiment-3/AMEY_B-50_DCL_EXPERIMENT-3.pdf) |
| 2 | client.py | RMI client implementation | [View](Distributed%20Computing%20Lab/Experiment-3/client.py) | — |
| — | Kaggle | Interactive notebook | [Explore](https://www.kaggle.com/ameythakur20/calculator-application-using-rmi) | — |

---

### Experiment-4: Lamport's Logical Clock
Implementation of LCS for event ordering in distributed systems.

| # | Program | Description | Source Code | Report |
|:-:|:---|:---|:-:|:-:|
| 1 | LCS.py | Logical Clock Synchronization | [View](Distributed%20Computing%20Lab/Experiment-4/LCS.py) | [View](Distributed%20Computing%20Lab/Experiment-4/AMEY_B-50_DCL_EXPERIMENT-4.pdf) |
| 2 | LCS-Connor.py | Alternative implementation | [View](Distributed%20Computing%20Lab/Experiment-4/LCS-Connorwstein.py) | — |
| — | Kaggle | Interactive notebook | [Explore](https://www.kaggle.com/ameythakur20/lamport-s-logical-clock-lcs) | — |

---

### Experiment-5: Bully Algorithm
Implementation of the Bully Election Algorithm for coordinator selection.

| # | Program | Description | Source Code | Report |
|:-:|:---|:---|:-:|:-:|
| 1 | Bully.java | Election algorithm implementation | [View](Distributed%20Computing%20Lab/Experiment-5/Bully.java) | [View](Distributed%20Computing%20Lab/Experiment-5/AMEY_B-50_DCL_EXPERIMENT-5.pdf) |

---

### Experiment-6: Token Ring Algorithm
Implementation of the Token Ring Algorithm for distributed mutual exclusion.

| # | Program | Description | Source Code | Report |
|:-:|:---|:---|:-:|:-:|
| 1 | TokenRing.java| Mutual exclusion implementation | [View](Distributed%20Computing%20Lab/Experiment-6/TokenRing.java) | [View](Distributed%20Computing%20Lab/Experiment-6/AMEY_B-50_DCL_EXPERIMENT-6.pdf) |

---

### Experiment-7: Chandy-Misra-Haas Algorithm
Implementation of edge-chasing algorithm for deadlock detection.

| # | Program | Description | Source Code | Report |
|:-:|:---|:---|:-:|:-:|
| 1 | Deadlock.py | Deadlock detection (CMH) | [View](Distributed%20Computing%20Lab/Experiment-7/ChandyMisraHaas%20(Deadlock).py) | [View](Distributed%20Computing%20Lab/Experiment-7/AMEY_B-50_DCL_EXPERIMENT-7.pdf) |
| 2 | NoDeadlock.py | No-deadlock scenario (CMH) | [View](Distributed%20Computing%20Lab/Experiment-7/ChandyMisraHaas%20(No%20Deadlock).py) | — |
| — | Kaggle | Deadlock scenario | [Explore](https://www.kaggle.com/ameythakur20/chandy-misra-haas-algorithm-deadlock) | — |

---

### Experiment-8: Load Balancing
Implementation of static and dynamic load balancing strategies.

| # | Program | Description | Source Code | Report |
|:-:|:---|:---|:-:|:-:|
| 1 | LoadBal.java | Java implementation | [View](Distributed%20Computing%20Lab/Experiment-8/LoadBalancing.java) | [View](Distributed%20Computing%20Lab/Experiment-8/AMEY_B-50_DCL_EXPERIMENT-8.pdf) |
| 2 | LoadBal.py | Python implementation | [View](Distributed%20Computing%20Lab/Experiment-8/LoadBalancing.py) | — |
| — | Kaggle | Performance analysis | [Explore](https://www.kaggle.com/ameythakur20/load-balancing) | — |

---

### Experiment-9: Distributed Systems Architecture
Review of architectural styles and system models.

| # | Program | Description | Report |
|:-:|:---|:---|:-:|
| — | Lab Report (PDF) | Detailed experiment report | [View](Distributed%20Computing%20Lab/Experiment-9/AMEY_B-50_DCL_EXPERIMENT-9.pdf) |

---

### Experiment-10: Name Resolution & RPC
Implementation of name services and remote procedure calls.

| # | Program | Description | Source Code | Report |
|:-:|:---|:---|:-:|:-:|
| 1 | RpcServer.py | RPC server logic | [View](Distributed%20Computing%20Lab/Experiment-10/RpcServer.py) | [View](Distributed%20Computing%20Lab/Experiment-10/AMEY_B-50_DCL_EXPERIMENT-10.pdf) |
| 2 | RpcClient.py | RPC client logic | [View](Distributed%20Computing%20Lab/Experiment-10/RpcClient.py) | — |
| 3 | Resolve.ipynb| Name resolution notebook | [View](Distributed%20Computing%20Lab/Experiment-10/Name_Resolution.ipynb) | — |
| — | Kaggle | Full implementation | [Explore](https://www.kaggle.com/code/ameythakur20/name-resolution) | — |

---

<!-- =========================================================================================
                                     RESEARCH PAPER SECTION
     ========================================================================================= -->
## Research Paper Presentation

>**Topic: A Comparative Study on Distributed File Systems**

| # | Resource | Description | Source |
|:-:|:---|:---|:-:|
| 1 | Research Paper | Full scholarly paper | [View](Research%20Paper%20Presentation/AMEY_B-50_DC_RPP/A_Comparative_Study_on_Distributed_File_Systems.pdf) |
| 2 | Presentation | Visual deck (PDF) | [View](Research%20Paper%20Presentation/AMEY_B-50_DC_RPP/A%20COMPARATIVE%20STUDY%20ON%20DISTRIBUTED%20FILE%20SYSTEMS.pdf) |

---

<!-- =========================================================================================
                                     ASSIGNMENTS SECTION
     ========================================================================================= -->
## Assignments

| # | Assignment | Description | Resource |
|:-:|:---|:---|:-:|
| 1 | Assignment - 1 | Fundamental DC Concepts | [View](Assignments/AMEY_B-50_DC_ASSIGNMENT-1.pdf) |
| 2 | Assignment - 2 | Communication & Synchronization | [View](Assignments/AMEY_B-50_DC_ASSIGNMENT-2.pdf) |
| 3 | Assignment - 3 | Replication & Fault Tolerance | [View](Assignments/AMEY_B-50_DC_ASSIGNMENT-3.pdf) |

---

<!-- =========================================================================================
                                     QUIZZES SECTION
     ========================================================================================= -->
## Quizzes

| # | Quiz | Topics | Resource |
|:-:|:---|:---|:-:|
| 1 | Quiz - 1 | Module - 1 | [View](Quizzes/DC_1_FH_22%5Bco1%5D.pdf) |
| 2 | Quiz - 2 | Module - 2 | [View](Quizzes/DC_2_FH_22%5Bco2%5D.pdf) |
| 3 | Quiz - 3 | Module - 3 | [View](Quizzes/DC_3_FH_22%5Bco3%5D.pdf) |
| 4 | Quiz - 4,5,6 | Module - 4 to 6 | [View](Quizzes/QUIZ%20II%20for%20Distributed%20Computing_Mod-IV%20to%20Mod-VI.pdf) |

---

<!-- =========================================================================================
                                     EXAMINATIONS SECTION
     ========================================================================================= -->
## Internal Assessment Tests

### IAT - 1
| # | Resource | Description | Link |
|:-:|:---|:---|:-:|
| — | Question Paper | IAT-1 Exam Paper | [View](IAT-1/DC%20IAT-1%20Question%20Paper.pdf) |
| 1 | Module - 1 | Introduction to DC | [View](IAT-1/DC_Module_1-Introduction_to_Distributed_Computing.pdf) |
| 2 | Module - 2 | Communication Models | [View](IAT-1/DC_Module_2-Communication.pdf) |
| 3 | Module - 3 | Synchronization Algorithms | [View](IAT-1/DC_Module_3-Synchronization.pdf) |

### IAT - 2
| # | Resource | Description | Link |
|:-:|:---|:---|:-:|
| — | Question Paper | IAT-2 Exam Paper | [View](IAT-2/DC_IAT-2_Question_Paper.pdf) |
| 1 | Question Bank 1 | DC Unit Test 2 QB | [View](IAT-2/DC_UT_2_QB.pdf) |
| 2 | Question Bank 2 | Comprehensive QB | [View](IAT-2/DC_QB.pdf) |

---

## Semester Exam

| # | Resource | Description | Link |
|:-:|:---|:---|:-:|
| 1 | Question Paper | University Exam Paper | [View](Semester%20Exam/DC_Question_Paper.pdf) |
| 2 | Question Bank | Theory/Subjective QB | [View](Semester%20Exam/DC_Question_Bank.pdf) |
| 3 | MCQ Bank | Solved Multiple Choice | [View](Semester%20Exam/DC_QB_SOLVED.pdf) |
| 4 | Timetable | Exam Schedule | [View](Semester%20Exam/Semester%208%20Timetable.pdf) |

---

<!-- =========================================================================================
                                     SUBMISSION SECTION
     ========================================================================================= -->
## Submission Report

| # | Document | Description | Link |
|:-:|:---|:---|:-:|
| 1 | Theory Report | Final Theory Submission | [View](Submission%20Report/Report_Viewer%20%5BTheory%5D.pdf) |
| 2 | Laboratory Report| Final Lab Submission | [View](Submission%20Report/Report_Viewer%20%5BLaboratory%5D.pdf) |
| 3 | Exit Survey | Course & Lab Evaluation | [View](Submission%20Report/Distributed%20Computing%20Exit%20Survey.pdf) |
| 4 | DC Report | Subject Submission Report | [View](Submission%20Report/AMEY_B-50_DC_SUBMISSION_REPORT.pdf) |
| 5 | Semester Report | Sem-VIII consolidated | [View](Submission%20Report/Amey_B-50_Submission_Report.pdf) |

---

## License

This repository and all linked academic content are made available under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. See the [LICENSE](LICENSE) file for complete terms.

> [!NOTE]
> **Summary:** You are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate attribution to the original author.

---

<!-- =========================================================================================
                                     FOOTER SECTION
     ========================================================================================= -->
<div align="center">

  <!-- Footer Navigation -->
  [↑ Back to Top](#distributed-computing--lab)

  [The Wall](#the-wall) &nbsp;·&nbsp; [Learning Path](#learning-path) &nbsp;·&nbsp; [Laboratory](#distributed-computing-laboratory) &nbsp;·&nbsp; [RPP](#research-paper-presentation) &nbsp;·&nbsp; [Quizzes](#quizzes) &nbsp;·&nbsp; [IAT](#iat---1) &nbsp;·&nbsp; [Exam](#semester-exam) &nbsp;·&nbsp; [Report](#submission-report)

  <br>

  🏠 **[Back to Computer Engineering](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)**

</div>

---

<div align="center">

  ### [Distributed Computing and Distributed Computing Laboratory](./)

  **CSC802 · CSL802 · Semester VIII · Computer Engineering**

  *University of Mumbai · Curated by [Amey Thakur](https://github.com/Amey-Thakur)*

</div>
