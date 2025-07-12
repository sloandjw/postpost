from src.file_loader import load_nc_file
from src.rule_parser import load_rules
from src.rule_engine import apply_rules
from src.file_writer import write_output

def main():
    input_path = "nc_files/input.nc"
    output_path = "nc_files/output.nc"
    rules_path = "rules/fanuc_default.yaml"

    lines = load_nc_file(input_path)
    rules = load_rules(rules_path)
    modified_lines = apply_rules(lines, rules)
    write_output(modified_lines, output_path)

if __name__ == "__main__":
    main()
