
import os
import pandas as pd
import numpy as np
import pdfplumber
from pathlib import Path
from absl import app, logging


dir_path = Path('C:\\Users\\User\\Desktop\\backup\\brt\\Projects\\Extract_grade_pdf_transcript\\110 030')

book_name = ['030012', '030022', '030032', '030042', '030052', '030062', '030072', '030082', '030092', '030102', '030112', '030122', '030132', '030142', '030152', '030162', '030172', '030182', '030192', '030202', '030212']
# book_name = ['030022', '030032', '030042', '030052']
# book_name = ['030032']

df_column_name = ["單位代碼", "應試號碼",
                  "高一上班排",	"高一上班人數", "高一上班排_百分比", "高一上類組(群)排", "高一上類組(群)人數", "高一上類組(群)排_百分比", "高一上校排", "高一上校人數", "高一上校排_百分比",
                  "高一下班排",	"高一下班人數", "高一下班排_百分比", "高一下類組(群)排", "高一下類組(群)人數", "高一下類組(群)排_百分比", "高一下校排", "高一下校人數", "高一下校排_百分比",
                  "高二上班排",	"高二上班人數",	"高二上班排_百分比", "高二上類組(群)排", "高二上類組(群)人數", "高二上類組(群)排_百分比", "高二上校排",	"高二上校人數",	"高二上校排_百分比",
                  "高二下班排",	"高二下班人數",	"高二下班排_百分比", "高二下類組(群)排", "高二下類組(群)人數", "高二下類組(群)排_百分比", "高二下校排", "高二下校人數", "高二下校排_百分比",
                  "高三上班排",	"高三上班人數",	"高三上班排_百分比", "高三上類組(群)排", "高三上類組(群)人數", "高三上類組(群)排_百分比", "高三上校排", "高三上校人數", "高三上校排_百分比",
                  "高三下班排",	"高三下班人數",	"高三下班排_百分比", "高三下類組(群)排", "高三下類組(群)人數", "高三下類組(群)排_百分比", "高三下校排",	"高三下校人數",	"高三下校排_百分比"]
df = pd.DataFrame(
    columns=df_column_name
    )

error_id = []
error_student_id = []
error_status = []

def appending_list(df_main_list, score_list, total_list):
    score_list_index = 1
    total_list_index = 0
        # sub_list_1 = [score_list[1], total_list[0], score_list[1] / total_list[0] * 100,
        #          score_list[2], total_list[1], score_list[2] / total_list[1] * 100,
        #          total_list[3], total_list[2], score_list[3] / total_list[2] * 100]
        # sub_list_2 = [score_list[8], total_list[3], score_list[8] / total_list[3] * 100,
        #          score_list[9], total_list[4], score_list[9] / total_list[4] * 100,
        #          total_list[10], total_list[5], score_list[10] / total_list[5] * 100]
    match len(total_list):
        case 10: # 北一女&三上
            for i in range(5):
                sub_list = [score_list[score_list_index], total_list[total_list_index], int(score_list[score_list_index]) / int(total_list[total_list_index]) * 100,
                        score_list[score_list_index+1], np.nan, np.nan,
                        score_list[score_list_index+2], total_list[total_list_index+1], int(score_list[score_list_index+2]) / int(total_list[total_list_index+1]) * 100]
                score_list_index += 7
                total_list_index += 2
            
                df_main_list.extend(sub_list)

            df_main_list.extend([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])        
            
        case 12: # 北一女&三下
            for i in range(6):
                sub_list = [score_list[score_list_index], total_list[total_list_index], int(score_list[score_list_index]) / int(total_list[total_list_index]) * 100,
                        score_list[score_list_index+1], np.nan, np.nan,
                        score_list[score_list_index+2], total_list[total_list_index+1], int(score_list[score_list_index+2]) / int(total_list[total_list_index+1]) * 100]
                score_list_index += 7
                total_list_index += 2
            
                df_main_list.extend(sub_list)
        
        case 15:
            match len(score_list):
                case 35: # 一般
                    for i in range(5):
                        sub_list = [score_list[score_list_index], total_list[total_list_index], int(score_list[score_list_index]) / int(total_list[total_list_index]) * 100,
                                score_list[score_list_index+1], total_list[total_list_index+1], int(score_list[score_list_index+1]) / int(total_list[total_list_index+1]) * 100,
                                score_list[score_list_index+2], total_list[total_list_index+2], int(score_list[score_list_index+2]) / int(total_list[total_list_index+2]) * 100]
                        score_list_index += 7
                        total_list_index += 3
                    
                        df_main_list.extend(sub_list)
                    
                    df_main_list.extend([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])        
                    # print(df_main_list)
                case 25: # 高雄中正高中
                    for i in range(5):
                        sub_list = [score_list[score_list_index], total_list[total_list_index], int(score_list[score_list_index]) / int(total_list[total_list_index]) * 100,
                                score_list[score_list_index+1], total_list[total_list_index+1], int(score_list[score_list_index+1]) / int(total_list[total_list_index+1]) * 100,
                                np.nan, total_list[total_list_index+2], np.nan]
                        score_list_index += 5
                        total_list_index += 3

                        df_main_list.extend(sub_list)
                    df_main_list.extend([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])

        case 18:
            match len(score_list):
                case 42: # 一般
                    for i in range(6):
                        sub_list = [score_list[score_list_index], total_list[total_list_index], int(score_list[score_list_index]) / int(total_list[total_list_index]) * 100,
                                score_list[score_list_index+1], total_list[total_list_index+1], int(score_list[score_list_index+1]) / int(total_list[total_list_index+1]) * 100,
                                score_list[score_list_index+2], total_list[total_list_index+2], int(score_list[score_list_index+2]) / int(total_list[total_list_index+2]) * 100]
                        score_list_index += 7
                        total_list_index += 3
                    
                        df_main_list.extend(sub_list)
                
                case 30: # 高雄中正高中
                    for i in range(6):
                        sub_list = [score_list[score_list_index], total_list[total_list_index], int(score_list[score_list_index]) / int(total_list[total_list_index]) * 100,
                                score_list[score_list_index+1], total_list[total_list_index+1], int(score_list[score_list_index+1]) / int(total_list[total_list_index+1]) * 100,
                                np.nan, total_list[total_list_index+2], np.nan]

                        score_list_index += 5
                        total_list_index += 3
                    
                        df_main_list.extend(sub_list)
                    
            # print(df_main_list)
    return df_main_list

def output(df, error_id, error_student_id, error_status):
    output_path = Path(dir_path, "output")
    df_without = pd.DataFrame({'單位代碼': error_id, "應試號碼": error_student_id, "備註": error_status})
    df_without.to_excel(Path(output_path, 'error_id.xlsx'), index=False)
    df.to_excel(Path(output_path, 'result.xlsx'), index=False)

def process_pdf(pdf_name, b, this_stud_id):
    os.chdir(Path(dir_path, b))
    try: 
        # logging.info(f'{b}  {pdf_name}')

        if pdf_name.startswith("頁面擷取自-"):
            this_stud_id = pdf_name[6:]
        else:
            this_stud_id = pdf_name[:8]
        
        _error_status = ""
        
        df_main_list = [b, this_stud_id]
        
        pdf = pdfplumber.open(f'{pdf_name}.pdf')
        page = pdf.pages[0]
        text = page.extract_text()   # 提取文字
        pdf.close()

        lines = text.split('\n')

        if('A0651R' in lines[0]):
            last_lines = lines[-4:-1]
            # last_lines = [line for line in last_lines if (('學業成績' in line) or ('總人數' in line))]
            score_lines = [line for line in last_lines if ('學業成績' in line)]
            # score_lines = last_lines[0]
            total_lines = [line for line in last_lines if ('總人數' in line)]
            # total_lines = last_lines[1]
            
            if (
                score_lines
                and total_lines
                ):
                score_list = score_lines[0].split(" ")[1:]
                total_list = total_lines[0].split(" ")[1:]
                # logging.info(len(score_list))
                # logging.info(len(total_list))
                
                df_main_list = appending_list(df_main_list, score_list, total_list)
                df.loc[len(df)] = df_main_list
                logging.info(f"{b}  {this_stud_id} worked!!")

            else:
                _error_status = f'score_lines and total_lines both false.'
                error_id.append(f'{b}')
                error_student_id.append(f'{this_stud_id}')
                error_status.append(f'{_error_status}')
                logging.info(f"{b}  {this_stud_id}  {_error_status}")

        else: 
            error_id.append(f'{b}')
            error_student_id.append(f'{this_stud_id}')
            if lines[0] == "":
                _error_status = f'Pictire.'
                error_status.append(f'{_error_status}')
                logging.info(f"{b}  {this_stud_id}  {_error_status}")
            else:
                _error_status = f'A0651R not in lines[0].'
                error_status.append(f'{_error_status}')
                logging.info(f"{b}  {this_stud_id}  {_error_status}")

    except Exception:
        _error_status = f'Error'
        error_id.append(f'{b}')
        error_student_id.append(f'{this_stud_id}')
        error_status.append(f'{_error_status}')
        logging.warning(f"{b}  {this_stud_id}  {_error_status}")


def process_directory(b, dir_path):
    os.chdir(Path(dir_path, b))
    
    list_file_name = sorted([item for item in os.listdir() if ".pdf" in item])
    new_list = [item[:-4] if item.endswith(".pdf") else item for item in list_file_name]
    # student_id = [( item[6:-4] if item.startswith("頁面擷取自-") else item[:8] if item.endswith(".pdf") else None) for item in list_file_name]
    # df_ = pd.DataFrame({'單位代碼':[f'{b}']* len(student_id),'應試號碼': student_id})
    # df_.to_excel(f'student_ids_{b}.xlsx', index=False)

    this_stud_id = None

    for pdf_name in new_list:
        process_pdf(pdf_name, b, this_stud_id)


def main(argv):
    for b in book_name:
        process_directory(b, dir_path)
    output(df, error_id, error_student_id, error_status)


if __name__ == '__main__':
    app.run(main)
