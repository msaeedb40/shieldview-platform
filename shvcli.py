#!/usr/bin/env python3
import sys
import subprocess
import argparse

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="ShieldView Platform CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Commands
    subparsers.add_parser("start", help="Start all services")
    subparsers.add_parser("stop", help="Stop all services")
    subparsers.add_parser("restart", help="Restart all services")
    subparsers.add_parser("status", help="Check status of services")
    subparsers.add_parser("health", help="Check system health")
    subparsers.add_parser("clean", help="Clean unused docker resources")
    subparsers.add_parser("logs", help="View service logs")
    subparsers.add_parser("link", help="Display platform service links")
    subparsers.add_parser("purge", help="Stop services and remove all data")

    args = parser.parse_args()

    if args.command == "start":
        print("Starting ShieldView Platform...")
        run_cmd("docker-compose up -d --build")
    elif args.command == "stop":
        print("Stopping services...")
        run_cmd("docker-compose down")
    elif args.command == "restart":
        print("Restarting services...")
        run_cmd("docker-compose restart")
    elif args.command == "status":
        run_cmd("docker-compose ps")
    elif args.command == "health":
        print("Checking health...")
        run_cmd("docker-compose ps") # Simple health check for now
    elif args.command == "clean":
        run_cmd("docker system prune -f")
    elif args.command == "purge":
        print("Purging system and data...")
        run_cmd("docker-compose down -v --rmi all --remove-orphans")
    elif args.command == "logs":
        run_cmd("docker-compose logs -f")
    elif args.command == "link":
        print("\n--- ShieldView Platform Links ---")
        print("Dashboard:  http://localhost:80")
        print("Middleware: http://localhost:8400")
        print("Backend:    http://localhost:8000")
        print("---------------------------------\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
