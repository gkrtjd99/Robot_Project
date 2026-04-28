# 01_Practice_Python

로봇 소프트웨어 개발을 위한 Python 기초부터 실전까지 다루는 실습 자료 모음입니다.  
Day1 ~ Day3에 걸쳐 기초 문법, OOP, 데이터 처리, 파일 I/O, 멀티스레딩까지 단계적으로 학습합니다.

---

## 목차

| 파일 | 주제 |
|------|------|
| [01.02.Python-Basic.ipynb](#0102python-basicipynb) | Python 기초 문법 |
| [01.03.Python-Practice.ipynb](#0103python-practiceipynb) | 실습: 계산기 CLI |
| [02.01.Python-Class.ipynb](#0201python-classipynb) | OOP · 클래스 · 상속 |
| [02.02.Python-NumPy.ipynb](#0202python-numpyipynb) | NumPy · Matplotlib |
| [02.03.Python-Data-Simulation.ipynb](#0203python-data-simulationipynb) | 실습: 센서 데이터 시뮬레이션 |
| [03.01.Python-File-JSON.ipynb](#0301python-file-jsonipynb) | 파일 I/O · JSON · 정규표현식 |
| [03.02.Python-Thread-Process.ipynb](#0302python-thread-processipynb) | 멀티스레딩 · 멀티프로세싱 |
| [03.03.Python-Sensor-Log.ipynb](#0303python-sensor-logipynb) | 실습: 센서 로그 파싱 & 시각화 자동화 |

---

## 노트북 상세

### 01.02.Python-Basic.ipynb
**Day1 · 블록2 · Python 기초 문법 실습**

| Part | 주제 |
|------|------|
| Part 1 | 자료형 · 변수 (int, float, str, bool, 컬렉션) |
| Part 2 | 제어문 (if · for · while · break · continue) |
| Part 3 | 함수와 예외 처리 (*args · **kwargs · lambda · try/except) |
| Part 4 | 퀴즈 & 복습 |

---

### 01.03.Python-Practice.ipynb
**Day1 · 블록3 · 실습: 계산기 CLI 만들기**

Sense-Think-Act 루프 구조를 익히며 계산기 CLI를 단계적으로 구현합니다.

| Part | 주제 |
|------|------|
| Part 1 | 실습 설계 및 요구사항 |
| Part 2 | 단계별 구현 (기본 입출력 → 함수 모듈화 → 예외 처리) |
| Part 3 | 오류 해결 & 심화 미션 |
| Part 4 | 로봇 SW 연결 (Sense-Think-Act) |

---

### 02.01.Python-Class.ipynb
**Day2 · 블록1 · OOP 입문 실습**

| Part | 주제 |
|------|------|
| Part 1 | 클래스 기초 (`__init__` · self · 인스턴스/클래스 변수) |
| Part 2 | 상속 · 추상화 (ABC · `@abstractmethod` · super() · MRO) |
| Part 3 | 퀴즈 & 복습 (다형성 · 컴포지션) |

---

### 02.02.Python-NumPy.ipynb
**Day2 · 블록2 · NumPy 배열 연산 & Matplotlib 실습**

| Part | 주제 |
|------|------|
| Part 1 | NumPy 필요성과 ndarray 구조 |
| Part 2 | 슬라이싱 · 불리언 인덱싱 · 브로드캐스팅 |
| Part 3 | 통계 연산 (mean · std · argmin · argmax) |
| Part 4 | 센서 데이터 처리 (LiDAR 극좌표 → 직교좌표 변환) |
| Part 5 | Matplotlib 시각화 (선 그래프 · 산점도 · 히스토그램) |
| Part 6 | 퀴즈 & 복습 |

---

### 02.03.Python-Data-Simulation.ipynb
**Day2 · 블록3 · 실습: 센서 데이터 시뮬레이션**

추상 클래스 기반 센서 계층 구조를 설계하고 LiDAR · IMU 데이터를 시뮬레이션합니다.

| Part | 주제 |
|------|------|
| Part 1 | 전체 구조 설계 (Sensor 추상 클래스) |
| Part 2 | 단계별 구현 (LiDAR · IMU · 이동평균 필터 · JSON 로깅) |
| Part 3 | 오류 해결 & 심화 미션 |
| Part 4 | Day3 연결 브리지 |

보조 스크립트: `02.03.Python-Plot.py`

---

### 03.01.Python-File-JSON.ipynb
**Day3 · 블록1 · 파일 I/O · JSON · 정규표현식 실습**

| Part | 주제 |
|------|------|
| Part 1 | 파일 I/O (open 모드 · with문 · pickle) |
| Part 2 | JSON 처리 (dump · load · dumps · loads · 예외 처리) |
| Part 3 | 정규표현식 (메타문자 · re.findall/sub · 그룹 캡처 · 로봇 로그 파싱) |
| Part 4 | 퀴즈 & 복습 |

---

### 03.02.Python-Thread-Process.ipynb
**Day3 · 블록2 · 멀티스레딩 · 멀티프로세싱 실습**

| Part | 주제 |
|------|------|
| Part 1 | 멀티태스킹 개념 (프로세스 vs 스레드 · GIL · 선택 기준) |
| Part 2 | 멀티스레딩 (Thread · Daemon · Lock · Thread-safe) |
| Part 3 | 멀티프로세싱 (Process · Pool · Queue · Event) |
| Part 4 | 퀴즈 & 복습 |

보조 스크립트:

| 파일 | 내용 |
|------|------|
| `03.02.01.Python-Thread-Daemon.py` | 데몬 스레드 예제 |
| `03.02.02.Python-Multi-Thread.py` | 멀티스레딩 센서 읽기 예제 |
| `03.02.03.Python-Process-Pool.py` | Pool 병렬 처리 예제 |
| `03.02.04.Python-Process-Queue.py` | 프로세스 간 Queue 통신 예제 |
| `03.02.05.PYthon-Thread-Practice.py` | 스레드 기반 센서 파이프라인 실습 |

---

### 03.03.Python-Sensor-Log.ipynb
**Day3 · 블록3 · 실습: 센서 로그 파싱 & 시각화 자동화**

JSON · 정규표현식 · OOP · NumPy · Matplotlib · 멀티스레딩을 통합하는 종합 실습입니다.

| Step | 주제 |
|------|------|
| Step 1 | JSON 설정 로드 & 정규표현식 (임계치 관리 · 비정형 텍스트 추출) |
| Step 2 | Sensor 클래스 통합 & 로그 파싱 (OOP · 정규식 활용) |
| Step 3 | NumPy 이상값 탐지 & Matplotlib 시각화 |
| Step 4 | 멀티스레딩 자동화 (백그라운드 분석 작업) |
| 부록 | Troubleshooting & 심화 미션 |

---

## 기타

- [venv_guide.md](venv_guide.md) — 가상환경 설정 가이드
