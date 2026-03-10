#!/usr/bin/env python3
"""Compute common PRC legal amounts."""

from __future__ import annotations

import argparse


def overdue_interest(args: argparse.Namespace) -> int:
    annual_rate = args.annual_rate
    if annual_rate is None:
        annual_rate = args.lpr + args.basis_points / 10000
    interest = args.principal * annual_rate * args.days / 365
    total = args.principal + interest
    print("逾期利息测算")
    print(f"- 本金: {args.principal:.2f}")
    print(f"- 年化利率: {annual_rate:.6f}")
    print(f"- 天数: {args.days}")
    print(f"- 利息: {interest:.2f}")
    print(f"- 本息合计: {total:.2f}")
    return 0


def labor_compensation(args: argparse.Namespace) -> int:
    compensation = args.monthly_wage * args.months * args.multiplier
    print("劳动争议补偿/赔偿测算")
    print(f"- 月工资基数: {args.monthly_wage:.2f}")
    print(f"- 月数: {args.months:.2f}")
    print(f"- 倍数: {args.multiplier:.2f}")
    print(f"- 金额: {compensation:.2f}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compute common PRC legal amounts.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    overdue = subparsers.add_parser("overdue-interest", help="Compute overdue interest.")
    overdue.add_argument("--principal", type=float, required=True)
    overdue.add_argument("--days", type=int, required=True)
    overdue.add_argument("--annual-rate", type=float)
    overdue.add_argument("--lpr", type=float, default=0.0, help="Annual LPR as decimal, e.g. 0.036")
    overdue.add_argument("--basis-points", type=float, default=0.0, help="Extra basis points over LPR.")
    overdue.set_defaults(func=overdue_interest)

    labor = subparsers.add_parser("labor-compensation", help="Compute labor compensation or damages.")
    labor.add_argument("--monthly-wage", type=float, required=True)
    labor.add_argument("--months", type=float, required=True)
    labor.add_argument("--multiplier", type=float, default=1.0, help="1 for compensation, 2 for damages, etc.")
    labor.set_defaults(func=labor_compensation)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
