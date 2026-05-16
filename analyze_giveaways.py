import json
import os
import glob
import re

def analyze_problems():
    files = glob.glob("problems/*.json")
    report = []

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:
                report.append(f"Error parsing {file_path}: {e}")
                continue

        file_name = os.path.basename(file_path)
        file_findings = []

        context_text = ""
        for key in ["context_md", "prompt_md", "body_md", "artifact_md"]:
            if key in data and data[key]:
                context_text += data[key] + " "

        blanks = data.get("blanks", {})
        if not blanks:
            continue

        for blank_key, blank_data in blanks.items():
            options = blank_data.get("distractors", []) + [blank_data.get("answer", "")]
            answer = blank_data.get("answer", "")
            if not options or not answer: continue

            findings = []
            ans_len = len(answer)
            distractor_lens = [len(opt) for opt in blank_data.get("distractors", [])]
            
            # (1) Length: 
            if distractor_lens:
                avg_dist_len = sum(distractor_lens)/len(distractor_lens)
                if ans_len > avg_dist_len + 12 or ans_len > avg_dist_len * 1.5:
                    findings.append(f"Correct answer ({ans_len} chars) is notably longer than distractors (avg {avg_dist_len:.1f} chars).")

            # (2) Verbatim Context:
            # Check if answer appears in prompt_md, body_md, artifact_md, or context_md
            # Ignore answers common in text like "Policy", "Standard" etc. unless they appear specifically as a 'giveaway'
            if answer.lower() in context_text.lower() and len(answer) > 4:
                # Basic check to see if it's literally handed to them
                findings.append(f"Correct answer '{answer}' appears verbatim in problem context.")

            # (3) Format Mismatch:
            types = set()
            for opt in options:
                if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", opt): types.add("IP")
                elif "/" in opt or "\\" in opt: types.add("Path")
                elif opt.isupper() and len(opt) > 2: types.add("Acronym")
                else: types.add("Text")
            
            if len(types) > 1:
                ans_type = "Text"
                if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", answer): ans_type = "IP"
                elif "/" in answer or "\\" in answer: ans_type = "Path"
                elif answer.isupper() and len(answer) > 2: ans_type = "Acronym"
                findings.append(f"Mixed option formats: {list(types)}. Answer is {ans_type}.")

            # (4) Specificity:
            ans_digits = len(re.findall(r"\d", answer))
            dist_digits = [len(re.findall(r"\d", opt)) for opt in blank_data.get("distractors", [])]
            if ans_digits > 0 and all(ds == 0 for ds in dist_digits):
                findings.append("Answer contains specific digits/metrics while distractors do not.")

            if findings:
                file_findings.append({"blank": blank_key, "options": options, "reasons": findings})

        if file_findings:
            report.append(f"--- {file_name} ---")
            for bf in file_findings:
                report.append(f"Blank: {bf['blank']} | Options: {bf['options']}")
                for r in bf['reasons']: report.append(f"  [!] {r}")
        else:
            report.append(f"--- {file_name} --- [Clean]")

    print("\n".join(report))

analyze_problems()
