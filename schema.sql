-- ─────────────────────────────────────────────────────────────
-- University Database Schema
-- Author  : Anish Rana Magar
-- Database: PostgreSQL 15+
-- Run with: psql -d university -f schema.sql
-- ─────────────────────────────────────────────────────────────

-- Drop tables in reverse dependency order (safe re-run)
DROP TABLE IF EXISTS TeachingAssignment CASCADE;
DROP TABLE IF EXISTS Enrolment          CASCADE;
DROP TABLE IF EXISTS Course             CASCADE;
DROP TABLE IF EXISTS Lecturer           CASCADE;
DROP TABLE IF EXISTS Student            CASCADE;
DROP TABLE IF EXISTS Department         CASCADE;

-- ── Department ────────────────────────────────────────────────
-- Stores academic departments. head_lecturer_id is set after
-- Lecturer rows exist (forward reference resolved by FK deferral).
CREATE TABLE Department (
    dept_id          SERIAL       PRIMARY KEY,
    name             VARCHAR(120) NOT NULL UNIQUE,
    head_lecturer_id INT          -- FK added below
);

-- ── Lecturer ──────────────────────────────────────────────────
CREATE TABLE Lecturer (
    lecturer_id SERIAL       PRIMARY KEY,
    name        VARCHAR(120) NOT NULL,
    email       VARCHAR(255) NOT NULL UNIQUE,
    dept_id     INT          NOT NULL REFERENCES Department(dept_id)
);

-- Resolve forward reference for Department.head_lecturer_id
ALTER TABLE Department
    ADD CONSTRAINT fk_head_lecturer
    FOREIGN KEY (head_lecturer_id) REFERENCES Lecturer(lecturer_id);

-- ── Student ───────────────────────────────────────────────────
CREATE TABLE Student (
    student_id  SERIAL       PRIMARY KEY,
    name        VARCHAR(120) NOT NULL,
    dob         DATE         NOT NULL,
    email       VARCHAR(255) NOT NULL UNIQUE,
    dept_id     INT          NOT NULL REFERENCES Department(dept_id)
);

-- ── Course ────────────────────────────────────────────────────
CREATE TABLE Course (
    course_id SERIAL       PRIMARY KEY,
    title     VARCHAR(200) NOT NULL,
    credits   SMALLINT     NOT NULL CHECK (credits BETWEEN 1 AND 30),
    dept_id   INT          NOT NULL REFERENCES Department(dept_id)
);

-- ── Enrolment (Student <-> Course, many-to-many) ─────────────
CREATE TABLE Enrolment (
    student_id INT           NOT NULL REFERENCES Student(student_id),
    course_id  INT           NOT NULL REFERENCES Course(course_id),
    semester   VARCHAR(10)   NOT NULL,          -- e.g. '2024-WS'
    grade      NUMERIC(4,2)  CHECK (grade BETWEEN 1.0 AND 5.0),
    PRIMARY KEY (student_id, course_id, semester)
);

-- ── TeachingAssignment (Lecturer <-> Course, many-to-many) ───
CREATE TABLE TeachingAssignment (
    lecturer_id INT         NOT NULL REFERENCES Lecturer(lecturer_id),
    course_id   INT         NOT NULL REFERENCES Course(course_id),
    semester    VARCHAR(10) NOT NULL,
    PRIMARY KEY (lecturer_id, course_id, semester)
);

-- ── Indexes ───────────────────────────────────────────────────
CREATE INDEX idx_enrolment_course    ON Enrolment(course_id);
CREATE INDEX idx_enrolment_semester  ON Enrolment(semester);
CREATE INDEX idx_course_dept         ON Course(dept_id);
CREATE INDEX idx_student_dept        ON Student(dept_id);
