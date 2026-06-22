# ============================================================
# GIT & GITHUB
# ============================================================

# Git is a Version Control System.
#
# Git helps track changes in code.
#
# GitHub is a cloud platform that stores
# Git repositories online.
#
# Why Learn Git?
#
# ✔ Track Code Changes
# ✔ Collaborate With Teams
# ✔ Backup Projects
# ✔ Industry Standard
# ✔ Required For Developers
#
# Install:
#
# https://git-scm.com/downloads
#
# Verify Installation:
#
# git --version

# ============================================================
# CHECK GIT VERSION
# ============================================================

# Command:
#
# git --version

# Example Output:
#
# git version 2.xx.x

# ============================================================
# CONFIGURE GIT
# ============================================================

# Set Username

# git config --global user.name "Your Name"

# Set Email

# git config --global user.email "your@email.com"

# Check Configuration

# git config --list

# ============================================================
# WHAT IS A REPOSITORY?
# ============================================================

# Repository (Repo)
#
# A folder tracked by Git.
#
# Example:
#
# AI_Project/
#
# Contains:
#
# Python Files
# Datasets
# Documentation
# Source Code

# ============================================================
# CREATE A REPOSITORY
# ============================================================

# Create Folder

# mkdir my_project

# Move Into Folder

# cd my_project

# Initialize Git

# git init

# ============================================================
# GIT INIT
# ============================================================

# Creates:
#
# .git/
#
# Hidden folder storing
# Git history and configuration.

# Example:
#
# git init

# ============================================================
# GIT STATUS
# ============================================================

# Shows:
#
# Modified Files
# New Files
# Deleted Files

# Command:
#
# git status

# ============================================================
# CREATE SAMPLE FILE
# ============================================================

# hello.py

print("Hello Git")

# ============================================================
# UNTRACKED FILES
# ============================================================

# After creating hello.py
#
# Run:
#
# git status
#
# Output:
#
# Untracked files:
#
# hello.py

# ============================================================
# GIT ADD
# ============================================================

# Add Specific File
#
# git add hello.py

# Add All Files
#
# git add .

# ============================================================
# STAGING AREA
# ============================================================

# Workflow:
#
# File
# ↓
# git add
# ↓
# Staging Area
# ↓
# git commit

# ============================================================
# GIT COMMIT
# ============================================================

# Save Snapshot Of Project

# Command:
#
# git commit -m "Initial Commit"

# Example:
#
# git commit -m "Added hello.py"

# ============================================================
# VIEW COMMIT HISTORY
# ============================================================

# Command:
#
# git log

# Short Version:
#
# git log --oneline

# ============================================================
# MODIFY FILE
# ============================================================

# hello.py

print("Hello GitHub")

# Run:
#
# git status

# Git detects modification.

# ============================================================
# COMMIT CHANGES
# ============================================================

# git add .
#
# git commit -m "Updated greeting"

# ============================================================
# GITHUB
# ============================================================

# GitHub stores repositories online.
#
# Website:
#
# https://github.com

# ============================================================
# CONNECT LOCAL REPOSITORY TO GITHUB
# ============================================================

# Example:
#
# git remote add origin
# https://github.com/username/project.git

# Check Remote:
#
# git remote -v

# ============================================================
# PUSH CODE TO GITHUB
# ============================================================

# First Push:
#
# git push -u origin main

# Later:
#
# git push

# ============================================================
# CLONE REPOSITORY
# ============================================================

# Download Repository

# Example:
#
# git clone
# https://github.com/user/project.git

# ============================================================
# GIT PULL
# ============================================================

# Download Latest Changes

# Command:
#
# git pull

# ============================================================
# GIT FETCH
# ============================================================

# Download Updates
#
# Without Merging

# Command:
#
# git fetch

# ============================================================
# BRANCHES
# ============================================================

# Branches allow parallel development.

# Main Branch:
#
# main

# Example:
#
# Feature Branch
# Bug Fix Branch
# Testing Branch

# ============================================================
# VIEW BRANCHES
# ============================================================

# Command:
#
# git branch

# ============================================================
# CREATE BRANCH
# ============================================================

# git branch feature-login

# ============================================================
# SWITCH BRANCH
# ============================================================

# git checkout feature-login

# OR
#
# git switch feature-login

# ============================================================
# CREATE + SWITCH
# ============================================================

# git checkout -b feature-login

# ============================================================
# MERGE BRANCH
# ============================================================

# Switch To Main
#
# git checkout main
#
# Merge
#
# git merge feature-login

# ============================================================
# DELETE BRANCH
# ============================================================

# git branch -d feature-login

# ============================================================
# .GITIGNORE
# ============================================================

# Ignore Files
#
# Example:
#
# __pycache__/
# .env
# venv/
# *.csv

# Create:
#
# .gitignore

# Example Content:

"""
venv/
__pycache__/
.env
*.csv
"""

# ============================================================
# PRACTICAL EXAMPLE 1
# AI PROJECT WORKFLOW
# ============================================================

# Create Project

# mkdir ai-chatbot

# cd ai-chatbot

# git init

# Create Files

# app.py
# requirements.txt

# Add Files

# git add .

# Commit

# git commit -m "Initial AI chatbot"

# ============================================================
# PRACTICAL EXAMPLE 2
# PUSH PROJECT TO GITHUB
# ============================================================

# Create Repository On GitHub
#
# ai-chatbot

# Connect

# git remote add origin
# https://github.com/username/ai-chatbot.git

# Push

# git push -u origin main

# ============================================================
# PRACTICAL EXAMPLE 3
# TEAM COLLABORATION
# ============================================================

# Clone Repository

# git clone repository_url

# Create Branch

# git checkout -b new-feature

# Make Changes

# Commit

# git commit -m "Added feature"

# Push

# git push origin new-feature

# ============================================================
# COMMON COMMANDS
# ============================================================

# git init
# git status
# git add .
# git commit -m
# git log
# git clone
# git push
# git pull
# git fetch
# git branch
# git checkout
# git merge

# ============================================================
# GIT WORKFLOW
# ============================================================

# Create File
#
# ↓
#
# git add .
#
# ↓
#
# git commit -m "message"
#
# ↓
#
# git push
#
# ↓
#
# GitHub

# ============================================================
# SUMMARY
# ============================================================

print("""
GIT & GITHUB SUMMARY

Configure Git:

git config --global user.name

git config --global user.email

Initialize Repository:

git init

Check Status:

git status

Add Files:

git add .

Commit Changes:

git commit -m "message"

Push To GitHub:

git push

Pull Changes:

git pull

Clone Repository:

git clone URL

Branch Commands:

git branch
git checkout
git merge

Important Concepts:

✔ Repository
✔ Commit
✔ Staging Area
✔ Branch
✔ Merge
✔ Remote Repository

Applications:

✔ Software Development
✔ AI Projects
✔ Team Collaboration
✔ Portfolio Building

Benefits:

✔ Version Control
✔ Backup Code
✔ Team Workflow
✔ Industry Standard
""")