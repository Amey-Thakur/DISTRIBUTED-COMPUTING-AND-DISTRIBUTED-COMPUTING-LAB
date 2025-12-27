<!-- =========================================================================================
                                     HEADER SECTION
     ========================================================================================= -->
<div align="center">
  
  # Distributed Computing Lab

  ### CSL802 · Semester VIII · Computer Engineering

  [![Curated by](https://img.shields.io/badge/Curated%20by-Amey%20Thakur-blue.svg)](https://github.com/Amey-Thakur)
  [![Documents](https://img.shields.io/badge/Documents-10-yellowgreen.svg)](#experiment-1-nos-vs-dos-comparison)
  [![Language](https://img.shields.io/badge/Language-Python%20%7C%20Java-blueviolet.svg)](./)
  [![Middleware](https://img.shields.io/badge/Middleware-Pyro4%20%7C%20RPC-orange.svg)](./)
  [![Type](https://img.shields.io/badge/Type-Code%20%7C%20PDF-brightgreen.svg)](./)

  **A comprehensive collection of laboratory experiments for Distributed Computing, covering clock synchronization, election algorithms, mutual exclusion, deadlock detection, and middleware protocols.**

  ---

  [How to Use](#how-to-use) &nbsp;·&nbsp; [Learning Path](#learning-path) &nbsp;·&nbsp; [Experiment-1](#experiment-1-nos-vs-dos-comparison) &nbsp;·&nbsp; [Experiment-2](#experiment-2-socket-programming-chat-app) &nbsp;·&nbsp; [Experiment-3](#experiment-3-rmi--rpc-implementation) &nbsp;·&nbsp; [Experiment-4](#experiment-4-logical-clock-synchronization) &nbsp;·&nbsp; [Experiment-5](#experiment-5-bully-election-algorithm) &nbsp;·&nbsp; [Experiment-6](#experiment-6-token-ring-mutual-exclusion) &nbsp;·&nbsp; [Experiment-7](#experiment-7-chandy-misra-haas-deadlock-detection) &nbsp;·&nbsp; [Experiment-8](#experiment-8-distributed-load-balancing) &nbsp;·&nbsp; [Experiment-9](#experiment-9-distributed-file-systems-case-study) &nbsp;·&nbsp; [Experiment-10](#experiment-10-name-resolution--rpc)

</div>

---

> [!TIP]
> **Distributed Architectures & Debugging**: This laboratory utilizes Python's `socket` module for low-level communication, `Pyro4` for RMI, and multithreaded Java for coordination protocols. When debugging these multi-process systems, use centralized logging or timestamped console outputs to trace events across nodes—logical clocks are essential for ordering in the absence of a global clock.

> [!WARNING]
> **Port Conflicts**: Ensure that ports used in the RMI and Socket experiments (default: 1234 or Pyro4 default) are not occupied by other system services. If a "Connection Refused" error occurs, verify that the server script is initialized and listening before running the client.

---

<!-- =========================================================================================
                                     HOW TO USE SECTION
     ========================================================================================= -->
## How to Use

### Viewing Implementation
1. **Navigate** to the specific experiment folder (e.g., `Experiment-7`).
2. **Execute** the script using the appropriate runtime:
   - **For Python**: `python Chat_Server.py` (Run server first, then client in a new terminal).
   - **For Java**: `javac Token_Ring.java && java Token_Ring`.
3. **Analyze** the console output to observe distributed protocol messages and state changes.

### Development Setup
**Required Tools:**
- **Python 3.x**: Standard library for sockets; `pip install Pyro4` for middleware tasks.
- **Java JDK 8+**: For multithreaded coordination implementations.
- **Terminal Multiplexer**: Recommended to run multiple nodes (processes) simultaneously for realistic simulation.

---

<!-- =========================================================================================
                                     LEARNING PATH SECTION
     ========================================================================================= -->
## Learning Path

### Phase 1: Communication & Middleware
Foundational concepts of process interaction and remote execution.
- **Experiment-1**: Compare Network vs Distributed Operating Systems.
- **Experiment-2**: Implement a multi-user Chat application using low-level Sockets.
- **Experiment-3**: Develop a remote Calculator service using RMI and RPC concepts.

### Phase 2: Synchronization & Coordination
Managing state and consensus in a distributed environment without global memory.
- **Experiment-4**: Synchronize events using Lamport's Logical Clocks.
- **Experiment-5**: Implement the Bully Algorithm for dynamic leader election.
- **Experiment-6**: Ensure Mutual Exclusion using the circular Token Ring protocol.

### Phase 3: Advanced Distributed Protocols
Handling complex scenarios like deadlocks, load distribution, and name services.
- **Experiment-7**: Detect distributed deadlocks using the Chandy-Misra-Haas edge-chasing algorithm.
- **Experiment-8**: Implement Static and Dynamic Load Balancing models.
- **Experiment-9**: Review Distributed File System architectures (NFS, AFS, GFS).
- **Experiment-10**: Implement Name Resolution and sophisticated RPC services.

---

<!-- =========================================================================================
                                     EXPERIMENT-1
     ========================================================================================= -->
## Experiment-1: NOS vs DOS Comparison

To Compare Network operating system and Distributed operating system.

**Date:** January 13, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-1/AMEY_B-50_DCL_EXPERIMENT-1.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-2
     ========================================================================================= -->
## Experiment-2: Socket Programming Chat App

To Implement Group Communication as a Chat application using socket programming.

**Date:** January 20, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Chat_Server.py | Multi-client chat server | [View](Experiment-2/Chat_Server.py) |
| 2 | Chat_Client.py | Interactive chat client | [View](Experiment-2/Chat_Client.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-2/AMEY_B-50_DCL_EXPERIMENT-2.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-3
     ========================================================================================= -->
## Experiment-3: RMI / RPC Implementation

To Implement any application using RMI/RPC.

**Date:** January 27, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | RMI_Server.py | Calculator service server | [View](Experiment-3/RMI_Server.py) |
| 2 | RMI_Client.py | Calculator service client | [View](Experiment-3/RMI_Client.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-3/AMEY_B-50_DCL_EXPERIMENT-3.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-4
     ========================================================================================= -->
## Experiment-4: Logical Clock Synchronization

To Implement Lamport Logical clock Algorithm.

**Date:** February 03, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Lamport_Clock_Synchronization.py | Lamport's Logical Clock | [View](Experiment-4/Lamport_Clock_Synchronization.py) |
| 2 | Lamport_Mutual_Exclusion.py | Alternative Clock implementation | [View](Experiment-4/Lamport_Mutual_Exclusion.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-4/AMEY_B-50_DCL_EXPERIMENT-4.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-5
     ========================================================================================= -->
## Experiment-5: Bully Election Algorithm

To Implement a Bully Algorithm.

**Date:** February 10, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Bully_Algorithm.java | Election protocol simulation | [View](Experiment-5/Bully_Algorithm.java) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-5/AMEY_B-50_DCL_EXPERIMENT-5.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-6
     ========================================================================================= -->
## Experiment-6: Token Ring Mutual Exclusion

To Implement Token Ring Mutual Exclusion Algorithm.

**Date:** February 18, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Token_Ring.java | Circular token passing engine | [View](Experiment-6/Token_Ring.java) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-6/AMEY_B-50_DCL_EXPERIMENT-6.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-7
     ========================================================================================= -->
## Experiment-7: Chandy-Misra-Haas Deadlock Detection

To Implement Chandi-Misra-Haas distributed deadlock detection algorithm.

**Date:** February 25, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Chandy_Misra_Haas.java | Unified CMH Simulation (Java) | [View](Experiment-7/Chandy_Misra_Haas.java) |
| 2 | Chandy_Misra_Haas_Deadlock.java | CMH (Deadlock - Java) | [View](Experiment-7/Chandy_Misra_Haas_Deadlock.java) |
| 3 | Chandy_Misra_Haas_No_Deadlock.java | CMH (No Deadlock - Java) | [View](Experiment-7/Chandy_Misra_Haas_No_Deadlock.java) |
| 4 | Chandy_Misra_Haas.py | Unified CMH Simulation (Python) | [View](Experiment-7/Chandy_Misra_Haas.py) |
| 5 | Chandy_Misra_Haas_Deadlock.py | CMH (Deadlock - Python) | [View](Experiment-7/Chandy_Misra_Haas_Deadlock.py) |
| 6 | Chandy_Misra_Haas_No_Deadlock.py | CMH (No Deadlock - Python) | [View](Experiment-7/Chandy_Misra_Haas_No_Deadlock.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-7/AMEY_B-50_DCL_EXPERIMENT-7.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-8
     ========================================================================================= -->
## Experiment-8: Distributed Load Balancing

To Implement Load Balancing algorithm.

**Date:** March 11, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Load_Balancing.java | Static load distribution (Java) | [View](Experiment-8/Load_Balancing.java) |
| 2 | Load_Balancing.py | Dynamic load balancer (Python) | [View](Experiment-8/Load_Balancing.py) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-8/AMEY_B-50_DCL_EXPERIMENT-8.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-9
     ========================================================================================= -->
## Experiment-9: Distributed File Systems Case Study

To Discuss different types of a file system (NFS, AFS, Google Case Study).

**Date:** March 18, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-9/AMEY_B-50_DCL_EXPERIMENT-9.pdf) |

---

<!-- =========================================================================================
                                     EXPERIMENT-10
     ========================================================================================= -->
## Experiment-10: Name Resolution & RPC

To Implement Name Resolution.

**Date:** March 31, 2022

| # | Program | Description | Source Code |
|:-:|:---|:---|:-:|
| 1 | Rpc_Server.py | Name Resolution Server | [View](Experiment-10/Rpc_Server.py) |
| 2 | Rpc_Client.py | Name Resolution Client | [View](Experiment-10/Rpc_Client.py) |
| 3 | Name_Resolution.ipynb | Jupyter Notebook version | [View](Experiment-10/Name_Resolution.ipynb) |
| 4 | test.txt | Dataset/Resource for resolution | [View](Experiment-10/Data/test.txt) |
| — | Lab Report (PDF) | Detailed experiment report | [View](Experiment-10/AMEY_B-50_DCL_EXPERIMENT-10.pdf) |

---

<!-- =========================================================================================
                                     FOOTER SECTION
     ========================================================================================= -->
<div align="center">

  <!-- Footer Navigation -->
  [↑ Back to Top](#distributed-computing-lab)

  [How to Use](#how-to-use) &nbsp;·&nbsp; [Learning Path](#learning-path) &nbsp;·&nbsp; [Experiment-1](#experiment-1-nos-vs-dos-comparison) &nbsp;·&nbsp; [Experiment-2](#experiment-2-socket-programming-chat-app) &nbsp;·&nbsp; [Experiment-3](#experiment-3-rmi--rpc-implementation) &nbsp;·&nbsp; [Experiment-4](#experiment-4-logical-clock-synchronization) &nbsp;·&nbsp; [Experiment-5](#experiment-5-bully-election-algorithm) &nbsp;·&nbsp; [Experiment-6](#experiment-6-token-ring-mutual-exclusion) &nbsp;·&nbsp; [Experiment-7](#experiment-7-chandy-misra-haas-deadlock-detection) &nbsp;·&nbsp; [Experiment-8](#experiment-8-distributed-load-balancing) &nbsp;·&nbsp; [Experiment-9](#experiment-9-distributed-file-systems-case-study) &nbsp;·&nbsp; [Experiment-10](#experiment-10-name-resolution--rpc)

  <br>

  🏠 **[Back to Main Repository](../)**

</div>

---

<div align="center">

  ### [Distributed Computing and Distributed Computing Laboratory](../)

  **CSL802 · Semester VIII · Computer Engineering**

  *University of Mumbai · Curated by [Amey Thakur](https://github.com/Amey-Thakur)*

</div>
